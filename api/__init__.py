import os
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv
from baseApi import baseApi
from flasgger import Swagger
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager
ENV_FILE = find_dotenv()
if ENV_FILE:
    ENV_FILE = load_dotenv()
app = Flask(__name__)
app.config.from_object(config.ENV)
app.config["SECRET_KEY"] = os.urandom(24)
db = SQLAlchemy(app)
app.logger #initialize logger
ma = Marshmallow(app)
CORS(app)#Init CORS
jwt = JWTManager(app)#Init JWT
from encoder import CustomJSONEncoder
app.json_encoder = CustomJSONEncoder

api = baseApi(app)


#Swagger api documentation
app.config['SWAGGER'] = {
    'title': 'PFA API Documentaion',
    'uiversion': 2
}

SWAGGER_DISPLAY = app.config['SWAGGER_DISPLAY']
if SWAGGER_DISPLAY ==1 :
    swagger_template = {'securityDefinitions': {'Bearer': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'}}}
    swagger = Swagger(app, template=swagger_template)

from logger_config import *
from .models.Users.UserModel import UserModel
from .models.Users.UserLogins import UserLogins
from .models.Ipl.Match import Match
from .models.Ipl.Deliveries import Deliveries
from .routes import *
