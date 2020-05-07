from datetime import datetime
import pandas as pd
import numpy as np
from api.schema.MatchSchema import match_schema
matchesdf = pd.read_csv('files/matches.csv')

matchesdf.rename(columns={'id':'import_id'}, inplace=True)
matchesdf.replace(np.nan, 'NaN', inplace=True)
matchesdf.dropna(inplace=True)
matchesdf = matchesdf[['import_id', 'season', 'city', 'date', 'team1', 'team2', 'toss_winner',
       'toss_decision', 'result', 'dl_applied', 'winner', 'win_by_runs',
       'win_by_wickets', 'player_of_match', 'venue', 'umpire1', 'umpire2']]
print(len(matchesdf.index))
matchesdf = matchesdf[matchesdf.import_id.apply(lambda x:str(x).isnumeric())]
matchesdf = matchesdf[matchesdf.dl_applied.apply(lambda x:str(x).isnumeric())]
matchesdf = matchesdf[matchesdf.win_by_runs.apply(lambda x:str(x).isnumeric())]
matchesdf = matchesdf[matchesdf.win_by_wickets.apply(lambda x:str(x).isnumeric())]

def check_valid_date(x):
  year, month, day = map(int, x.split('-'))
  try:
    datetime(year, month, day)
    return True
  except:
    return False

matchesdf = matchesdf[matchesdf.date.apply(check_valid_date)]
for index, row in matchesdf.iterrows():
  row = row.to_dict()
  row = match_schema.load(row)
  res = row.save()
