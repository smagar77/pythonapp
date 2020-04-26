from celery import Celery
capp = Celery('tasks', broker='amqp://localhost/', backend='db+postgresql://postgres:postgres@localhost/test')

@capp.task(name="testing...")
def reverse(string):
    return string[::-1]
