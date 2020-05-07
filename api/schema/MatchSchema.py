from marshmallow import fields
from api import ma
from api.models.Ipl.Match import Match

class Match(ma.ModelSchema):
    '''MatchSchema class handle users schema'''
    class Meta:
        model = Match

    id = fields.Integer()
    season = fields.Integer()
    city = fields.String()
    date = fields.String()
    team1 = fields.String()
    team2 = fields.String()
    toss_winner = fields.String()
    toss_decision = fields.String()
    result = fields.String()
    dl_applied = fields.Integer()
    winner = fields.String()
    win_by_runs = fields.Integer()
    win_by_wickets = fields.Integer()
    player_of_match = fields.String()
    venue = fields.String()
    umpire1 = fields.String()
    umpire2 = fields.String()
    import_id = fields.Integer()

match_schema = Match()
