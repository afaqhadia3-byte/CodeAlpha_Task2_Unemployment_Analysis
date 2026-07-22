# Task 2: Unemployment Analysis with Python

# Import libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data set:
df = pd.read_csv("Unemployment in india.csv")

# Display first five rows:
df.head()

# Check dataset information:
df.info()

# statistical summary:
df.describe()

# check missing values:
df.isnull().sum()
df.dropna(inplace=True)

# Remove extra spaces from column names:
df.columns = df.columns.str.strip()

# Convert data columns:
df["Date"] = pd.to_datetime(df["Date"])

# Check duplicate rows:
df.duplicated().sum()

df.drop_duplicates(inplace=True)

# Average unemployment rate:
df["Estimated Unemployment Rate (%)"].mean()

# Highest and lowest unemployment:
print(df["Estimated Unemployment Rate (%)"].max())
print(df["Estimated Unemployment Rate (%)"].min())

# unemployment trend over time:
plt.figure(figsize=(12,6))

plt.plot(df["Date"],
         df["Estimated Unemployment Rate (%)"])

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)

plt.show()

# State-wise average unemployment:
state_avg = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

state_avg.plot(kind="bar", figsize=(12,6))

plt.title("Average Unemployment by State")
plt.xlabel("State")
plt.ylabel("Average Rate")
plt.show()

# Covid-19 Analysis:
covid = df[df["Date"] >= "2020-03-01"]

plt.figure(figsize=(12,6))

sns.lineplot(data=covid,
             x="Date",
             y="Estimated Unemployment Rate (%)")

plt.title("Impact of COVID-19 on Unemployment")

plt.show()

# Distribution of unemployment:
sns.histplot(df["Estimated Unemployment Rate (%)"],
             bins=20,
             kde=True)

plt.show()

#create heatmap:
pivot = df.pivot_table(values="Estimated Unemployment Rate (%)",
                       index="Region",
                       columns="Date")

plt.figure(figsize=(14,8))

sns.heatmap(pivot,
            cmap="YlOrRd")

plt.show()

# Monthly average unemployment
df["Month"] = df["Date"].dt.month_name()

monthly_avg = df.groupby("Month")["Estimated Unemployment Rate (%)"].mean()

plt.figure(figsize=(10,5))
monthly_avg.plot(kind="bar", color="skyblue")

plt.title("Monthly Average Unemployment Rate")
plt.xlabel("Month")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=45)

plt.show()

print("\nConclusion:")
print("• The unemployment data was successfully analyzed using Python.")
print("• Unemployment rates increased significantly during the COVID-19 period.")
print("• Different regions experienced different unemployment levels.")
print("• Monthly analysis showed fluctuations in unemployment trends.")
print("• These insights can help policymakers understand employment patterns and make better economic decisions.")