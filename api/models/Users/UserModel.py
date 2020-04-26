from api import db
from api.models.mixin import ModelMixin
class UserModel(db.Model, ModelMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    created_on = db.Column(db.DateTime(timezone=True))
    user_logins = db.relationship('UserLogins', backref='UserModel', lazy='subquery')
    __table_args__ = (db.UniqueConstraint('username'),)