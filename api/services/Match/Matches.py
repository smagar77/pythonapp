import logging
from sqlalchemy.orm import noload
from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import jwt_required
from api.models.Ipl.Match import Match as MatchModel
from api.schema.MatchSchema import match_schema
class Match(Resource):

  @jwt_required
  def get(self):
    matches = MatchModel.query.options(noload('*')).order_by('id').all()
    matches = [match_schema.dump(match_row) for match_row in matches ]
    return jsonify({'count':matches})
