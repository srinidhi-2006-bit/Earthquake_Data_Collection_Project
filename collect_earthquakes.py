import requests
import pandas as pd
from datetime import datetime, timedelta
import os
import json

if not os.path.exists("data"):
    os.makedirs("data")

start = (datetime.utcnow() - timedelta(days=30)).strftime("%Y-%m-%d")
end = datetime.utcnow().strftime("%Y-%m-%d")
url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start}&endtime={end}&minmagnitude=3.5"

r = requests.get(url, timeout=30)
data = r.json()
features = data.get("features", [])

rows = []
for f in features:
    props = f.get("properties", {})
    geom = f.get("geometry", {})
    coords = geom.get("coordinates", [None, None, None])
    rows.append({
        "id": f.get("id"),
        "time_utc": datetime.utcfromtimestamp(props.get("time", 0)/1000).isoformat(),
        "latitude": coords[1],
        "longitude": coords[0],
        "depth_km": coords[2],
        "magnitude": props.get("mag"),
        "place": props.get("place"),
        "url": props.get("url"),
        "type": props.get("type")
    })

df = pd.DataFrame(rows)
csv_name = f"data/earthquakes_{start}_to_{end}.csv"
json_name = f"data/earthquakes_{start}_to_{end}.json"

df.to_csv(csv_name, index=False)
with open(json_name, "w") as f:
    json.dump(data, f)

print("Saved:", csv_name, json_name)
print(df.head(10).to_string(index=False))
