from api import db
import pandas as pd
from api.models.Ipl.Deliveries import Deliveries
from api.models.Ipl.Match import Match
data = db.session.query(Match.id, Match.import_id, Deliveries.id.label('deliveries_id')).join(Deliveries).filter().all()
filtered_data = pd.DataFrame(data)
filtered_data.to_csv('update_ids.csv', index=False)
