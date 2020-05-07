from datetime import datetime
import pandas as pd
import numpy as np
from api.schema.DeliveriesScheme import deliveries_schema
matchesdf = pd.read_csv('files/deliveries.csv')
matchesdf.replace(np.nan, 'NaN', inplace=True)
matchesdf.dropna(inplace=True)
i=0
for index, row in matchesdf.iterrows():
  if i==0:
    i+=1
    continue
  row = row.to_dict()
  row = deliveries_schema.load(row)
  res = row.save()
  print(res)
