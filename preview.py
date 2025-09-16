import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

if not os.path.exists("output"):
    os.makedirs("output")

start = (datetime.utcnow() - timedelta(days=30)).strftime("%Y-%m-%d")
end = datetime.utcnow().strftime("%Y-%m-%d")
csv_file = f"data/earthquakes_{start}_to_{end}.csv"

df = pd.read_csv(csv_file)
df = df.dropna(subset=["latitude", "longitude", "magnitude"])

plt.figure(figsize=(10,6))
plt.scatter(df["longitude"], df["latitude"], s=(df["magnitude"]**2)*4)
plt.title("Earthquakes: last 30 days (bubble size ~ magnitude^2)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)

plot_file = f"output/earthquakes_plot.png"
plt.savefig(plot_file)
plt.show()

print("Plot saved at:", plot_file)
