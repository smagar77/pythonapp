from datetime import datetime, timedelta
import logging
from flask_restful import Resource, reqparse
from flask import jsonify, request
from api.schema.UserSchema import user_schema
from api.models.Users.UserModel import UserModel
from flask_jwt_extended import create_access_token,jwt_required
logger = logging.getLogger(__name__)
parser = reqparse.RequestParser()
parser.add_argument('username', required=True)
parser.add_argument('password', required=True)
parser.add_argument('first_name')
parser.add_argument('last_name', required=True)
parser.add_argument('email', required=True)
class User(Resource):
    def get(self, id=None):
        '''Retrieve all users(GET method)'''
        if id is not None:
            data = UserModel.query.filter_by(id=id).order_by('id').all()
        else:
            data = UserModel.query.order_by('id').all()
        result = [user_schema.dump(user) for user in data]
        return jsonify(result)

    def post(self):
        '''Save new user'''
        if not request.is_json:
            return {"error":True, "status":400, "message":"Content-Type should be application/json"}, 400
        json_request = request.get_json(force=True)
        try:
            data = user_schema.load(json_request)
            save_data_result = data.save()
            if save_data_result is not None:
                result = {"status": "success", "message": save_data_result}
            else:
                result = {"status": "success", "message": "Unable to save user"}
        except Exception as e:
            result = {"status":"failed", "message":"User creation failed, error:"+str(e)}
        return jsonify(result)

    def delete(self, id=None):
        if id is not None:
            try:
                user = UserModel.query.get(id)
                print(user)
                user.delete()
                return jsonify({'message':'User deleted successfully'})
            except Exception as e:
                return jsonify({'message':str(e)})

class UserLogin(Resource):

  def post(self):
    if not request.is_json:
      return {"error":True, "status":400, "message":"Content-Type should be application/json"}, 400
    user = UserModel.query.filter_by(**request.get_json(force=True)).first()
    if user:
      expires = timedelta(hours=10)
      json_request = request.get_json(force=True)
      access_token = create_access_token(json_request, expires_delta=expires)
      return jsonify({'userid':user.id, 'access_token':access_token})
    return jsonify({'message':'user login failed'}), 401
