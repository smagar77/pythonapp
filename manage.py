import os
import unittest
import logging
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import app, db
logger = logging.getLogger(__name__)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def test(path=None):
  os.environ['TEST_DIR'] = os.path.abspath('test')
  path = path.replace(".", "/") if path else "test"

  tests = unittest.TestLoader().discover(path)
  unittest.TextTestRunner(verbosity=2).run(tests)


if(__name__ == '__main__'):
    manager.run()
