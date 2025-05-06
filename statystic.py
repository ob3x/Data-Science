import matplotlib.pyplot as plt
import pandas as pd

raw_data = pd.read_csv("weatherHistory.csv")
df = pd.DataFrame(raw_data)

hotest = df[df["Temperature (C)"] == df["Temperature (C)"].max()]

print(df[df["Precip Type"] == "snow"])
