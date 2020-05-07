import unittest
from mockito import unstub
from api import app
class BaseTest(unittest.TestCase):
  def setUp(self) -> None:
    self.client = app.test_client()
    app.app_context()

  def tearDown(self) -> None:
    unstub()
