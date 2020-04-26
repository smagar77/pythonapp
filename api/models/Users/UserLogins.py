from api import db
from api.models.mixin import ModelMixin
class UserLogins(db.Model, ModelMixin):
    __tablename__ = 'user_logins'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    login_date = db.Column(db.DateTime(timezone=True))