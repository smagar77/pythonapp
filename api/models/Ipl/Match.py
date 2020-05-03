import datetime
from api import db
from api.models.mixin import ModelMixin
class Match(db.Model, ModelMixin):
  __talename__='match'
  id = db.Column(db.Integer, primary_key=True)
  season = db.Column(db.String(255))
  city = db.Column(db.String(255))
  date = db.Column(db.Date, default=datetime.date.today())
  team1 = db.Column(db.String(255))
  team2 = db.Column(db.String(255))
  toss_winner = db.Column(db.String(255))
  toss_decision = db.Column(db.String(255))
  result = db.Column(db.String(255))
  dl_applied = db.Column(db.Integer)
  winner = db.Column(db.String(255))
  win_by_runs = db.Column(db.Integer)
  win_by_wickets = db.Column(db.Integer)
  player_of_match = db.Column(db.String(255))
  venue = db.Column(db.String(255))
  umpire1 = db.Column(db.String(255))
  umpire2 = db.Column(db.String(255))
  deliveries = db.relationship('Deliveries', backref='Match', lazy='joined')
