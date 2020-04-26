import logging
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import app, db
logger = logging.getLogger(__name__)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if(__name__ == '__main__'):
    manager.run()