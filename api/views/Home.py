from flask_restful import Resource
from flask import jsonify
from api import db
class Home(Resource):
    def get(self):
        return jsonify({'message':db.session.autoflush})