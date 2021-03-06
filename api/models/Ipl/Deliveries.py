from api import db
from api.models.mixin import ModelMixin
class Deliveries(db.Model, ModelMixin):

  id = db.Column(db.Integer, primary_key=True)
  match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
  inning = db.Column(db.Integer)
  batting_team = db.Column(db.String(255))
  bowling_team = db.Column(db.String(255))
  over = db.Column(db.Integer)
  ball = db.Column(db.Integer)
  batsman = db.Column(db.String(255))
  non_striker = db.Column(db.String(255))
  bowler = db.Column(db.String(255))
  is_super_over = db.Column(db.Boolean)
  wide_runs = db.Column(db.Integer)
  bye_runs = db.Column(db.Integer)
  legbye_runs = db.Column(db.Integer)
  noball_runs = db.Column(db.Integer)
  penalty_runs = db.Column(db.Integer)
  batsman_runs = db.Column(db.Integer)
  extra_runs = db.Column(db.Integer)
  total_runs = db.Column(db.Integer)
  player_dismissed = db.Column(db.String(555))
  dismissal_kind = db.Column(db.String(555))
  fielder = db.Column(db.String(255))
