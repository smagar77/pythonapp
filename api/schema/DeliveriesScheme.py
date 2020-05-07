from marshmallow import fields
from api import ma
from api.models.Ipl.Deliveries import Deliveries

class Deliveries(ma.ModelSchema):
    '''MatchSchema class handle users schema'''
    class Meta:
        model = Deliveries

    id = fields.Integer()
    match_id = fields.Integer()
    inning = fields.Integer()
    batting_team = fields.String()
    bowing_team = fields.String()
    over = fields.Integer()
    ball = fields.Integer()
    batsman = fields.String()
    non_striker = fields.String()
    bowler = fields.String()
    is_super_over = fields.Integer()
    wide_runs = fields.Integer()
    bye_runs = fields.Integer()
    legbye_runs = fields.Integer()
    noball_runs = fields.Integer()
    penalty_runs = fields.Integer()
    batsman_runs = fields.Integer()
    extra_runs = fields.Integer()
    total_runs = fields.Integer()
    player_dismissed = fields.String()
    dismissal_kind = fields.String()
    fielder = fields.String()

deliveries_schema = Deliveries()
