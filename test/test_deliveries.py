from base_test import BaseTest
from unittest.mock import patch, MagicMock
from api.services.Match.Deliveries import Deliveries

def verify_jwt_in_request(match_id):
  return

class TestDeliveries(BaseTest):
  @patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
  def test_deliveries(self, *args):
    response = Deliveries.get(self, 2)
    self.assertEqual(response.status_code, 200)
