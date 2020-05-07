from base_test import BaseTest
from unittest.mock import patch
from api.services.Match.Matches import Match



class TestMatch(BaseTest):

  @patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
  def test_get(self, *args):
      response = Match.get(self)
      self.assertEqual(response.status_code, 200)
