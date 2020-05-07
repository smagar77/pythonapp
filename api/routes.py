from api import api
from .views.Home import Home
from .services.Users import User, UserLogin
from api.services.Match.Matches import Match
from api.services.Match.Deliveries import Deliveries

api.add_resource(Home, '/', methods=['GET'])
user_api = [
    '/users/',
    '/users/add_user/',
    '/users/user/<int:id>/',
]

match_api = [
    '/matches/',
    '/match/add_match/',
    '/matches/match/<int:id>/',
]

api.add_resource(User, *user_api, methods=["GET", "POST","DELETE"])
api.add_resource(UserLogin, '/login/', methods=["POST"])
api.add_resource(Match, *match_api, methods=["GET", "POST","DELETE"])
api.add_resource(Deliveries, '/deliveries/<int:match_id>/', methods=["GET"])
