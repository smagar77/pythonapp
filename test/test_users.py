import json
import requests
from base_test import BaseTest
from unittest.mock import patch
from api.services.Users import User, UserLogin

class test_user(BaseTest):

  @patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
  def test_get(self, *args):
    result = User.get(self)
    result1 = User.get(self, 1)
    self.assertEqual(result.status_code, 200)
    self.assertEqual(result1.status_code, 200)

  @patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
  def test_post(self, *args):
    result = self.client.post('http://localhost:5000/users/add_user/', data=json.dumps({"":""}), headers={"Content-Type":"application/json", "Authorization":"Bearer {0}"})
    #self.assertEqual(result.status_code, 200)

  @patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')
  @patch('api.services.Users.User.delete_uesr')
  def test_delete(self, *args):
    result = self.client.delete('http://localhost:5000/users/user/5/', headers={"Content-Type":"application/json", "Authorization":"Bearer {0}"})
    self.assertEqual(result.status_code, 200)
