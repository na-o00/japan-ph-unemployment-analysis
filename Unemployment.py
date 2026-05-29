import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("unemployment_rate.csv")
print(df.head())

plt.figure(figsize = (10,8))

#Unemployment
plt.subplot(5,1,1)
plt.plot(df["Years"], df["Japan"], label = "Japan")
plt.plot(df["Years"], df["Philippines"], label = "Philippines")
df["Japan MA"] = df["Japan"].rolling(5).mean()
plt.plot(df["Years"], df["Japan MA"], linestyle = "--", label = "Japan MA")
df["Philippines MA"] = df["Philippines"].rolling(5).mean()
plt.plot(df["Years"], df["Philippines MA"], linestyle = "--", label = "Philippines MA")
plt.xlabel("Years")
plt.ylabel("Unemployment")
plt.title("Unemployment Comparison: Japan vs Philippines")
plt.legend()
plt.grid()

#Differences
plt.subplot(5,1,2)
df["Differences"] = df["Japan"] - df["Philippines"]
plt.plot(df["Years"], df["Differences"], label = "Unemployment gap")
plt.xlabel("Years")
plt.ylabel("Unemployment")
plt.title("Unemployment Gap: Japan - Philippines")
plt.legend()
plt.grid()

#Growth Rate
plt.subplot(5,1,3)
df["Japan Growth Rate"] = df["Japan"].pct_change()
plt.plot(df["Years"], df["Japan Growth Rate"], label = "Japan Growth Rate")
df["Philippines Growth Rate"] = df["Philippines"].pct_change()
plt.plot(df["Years"], df["Philippines Growth Rate"], label = "Philippines Growth Rate")
df["Japan Growth MA"] = df["Japan Growth Rate"].rolling(5).mean()
plt.plot(df["Years"], df["Japan Growth MA"], linestyle = "--", label = "Japan Growth Rate MA")
df["Philippines Growth MA"] = df["Philippines Growth Rate"].rolling(5).mean()
plt.plot(df["Years"], df["Philippines Growth MA"], linestyle = ":", label = "Philippines Growth Rate MA")
plt.xlabel("Years")
plt.ylabel("Growth Rate")
plt.title("Unemployment Growth Rate Comparison: Japan vs Philippines")
plt.legend()
plt.grid()

#Ratio
plt.subplot(5,1,4)
df["Ratio"] = df["Philippines"] / df["Japan"]
plt.plot(df["Years"], df["Ratio"], label = "Unemployment Ratio")
df["Ratio MA"] = df["Ratio"].rolling(5).mean()
plt.plot(df["Years"], df["Ratio MA"], linestyle = "--", label = "Unemployment Ratio MA")
plt.xlabel("Years")
plt.ylabel("Ratio")
plt.title("Unemployment Ratio")
plt.legend()
plt.grid()

#Scattergram
plt.subplot(5,1,5)
plt.scatter(df["Japan"], df["Philippines"])
m, b = np.polyfit(df["Japan"], df["Philippines"], 1)
plt.plot(df["Japan"], m*df["Japan"] + b)
plt.text(df["Japan"].min(), df["Philippines"].max(), f"Slope: {m: .3f}")
print(f"Slope: {m: .3f}")
correlation = np.corrcoef(df["Japan"], df["Philippines"]) [0,1]
print(f"Correlation: {correlation: .3f}")
plt.text(df["Japan"].min(), df["Philippines"].max()-2, f"Correlation: {correlation: .3f}")
plt.xlabel("Japan")
plt.ylabel("Philippines")
plt.title("Relationship between Japan and the Philippines Unemployment")
plt.grid()

JapanMax = df["Japan"].max()
JapanMin = df["Japan"].min()
print(f"Japan Max Value: {JapanMax: .3f}")
print(f"Japan Min Value: {JapanMin: .3f}")


plt.tight_layout()
plt.savefig("unemployment_analysis.png")
plt.show()
