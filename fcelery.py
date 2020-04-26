import logging
from api import app
from celery import Celery
from celery.schedules import crontab
import time

from api.models.Users.UserModel import UserModel

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)
logger = logging.getLogger(__name__)

@celery.task(name='celery auto insert user')
def add_user(**kwargs):
    '''A Celery task utility which will perform user creation'''
    user = UserModel(
        username=kwargs['username'],
        password=kwargs['password'],
        first_name=kwargs['first_name'],
        last_name=kwargs['last_name'],
        email=kwargs['email'],
    )
    try:
        result = user.save()
        return result
    except Exception as e:
        return str(e)

@celery.task(name='test addition task')
def add(*args):
    return args[0]+args[1]

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    '''A Celery beat method will setup tasks which will run priodically'''
    data = {
        'username': 'user' + str(time.time()),
        'password': 'user14' + str(time.time()),
        'first_name': 'user14Fname' + str(time.time()),
        'last_name': 'user14Lname' + str(time.time()),
        'email': 'user14@yopmail.com' + str(time.time())
    }

    sender.add_periodic_task(
        crontab(minute='*/1'), add.s(*{10, 20})
    )