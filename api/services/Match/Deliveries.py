import logging
import json
from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import jwt_required
from api.models.Ipl.Deliveries import Deliveries as DeliveriesModel
from api.schema.DeliveriesScheme import deliveries_schema
import pandas as pd
logger = logging.getLogger(__name__)
class Deliveries(Resource):

  @jwt_required
  def get(self, match_id):
    try:
      delv_data = DeliveriesModel.query.filter_by(match_id=match_id).order_by('id').all()
      delv_data = [ deliveries_schema.dump(row) for row in delv_data ]
      delv_data = pd.DataFrame(delv_data)
      delv_data.replace('NaN', '', inplace=True)
      delv_data = json.loads(delv_data.to_json(orient='records'))
      return jsonify(delv_data)
    except Exception as exp:
      logger.exception(str(exp))
