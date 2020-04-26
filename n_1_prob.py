# import logging
# from api import app
# import time
# from api import db
# import logging
# from sqlalchemy.orm import joinedload, subqueryload
# from api.models.Users.UserModel import UserModel
#
# logger = logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
#
# user_data = UserModel.query.all()
# for user in user_data:
#     for login in user.user_logins:
#         print(str(login))
dictn = {
    'key01':'val01',
    'key02':'val02',
    'key03':'val03',
    'key04':'val04',
    'key05':'val05',
}


print(hash(frozenset(dictn.items())))