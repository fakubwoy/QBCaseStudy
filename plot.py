import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

traffic_data = pd.read_csv("traffic_flow_data.csv")
signal_data = pd.read_csv("signal_timings_data.csv")

traffic_data["Hour"] = traffic_data["Hour"].astype(str)

total_traffic = traffic_data.groupby("Intersection")["Vehicle_Count"].sum().reset_index()
peak_hours = ["7", "8", "9", "17", "18", "19"]
traffic_peak = traffic_data[traffic_data["Hour"].isin(peak_hours)]
vehicle_distribution = traffic_peak.groupby("Vehicle_Type")["Vehicle_Count"].sum().reset_index()
merged_data = pd.merge(signal_data, total_traffic, on="Intersection")

traffic_pivot = traffic_data.pivot_table(index="Intersection", columns="Hour", values="Vehicle_Count", aggfunc="sum")

plt.figure(figsize=(12, 6))
sns.heatmap(traffic_pivot, cmap="Reds", linewidths=0.5, annot=True, fmt=".0f")
plt.title("Traffic Congestion Intensity at Intersections")
plt.xlabel("Hour of the Day")
plt.ylabel("Intersection")
plt.savefig("heatmap.png")  
plt.close()

plt.figure(figsize=(20, 5))
sns.barplot(data=traffic_peak, x="Hour", y="Vehicle_Count", hue="Vehicle_Type", palette="Set2")
plt.title("Vehicle Count by Type During Peak Hours")
plt.xlabel("Hour of the Day")
plt.ylabel("Vehicle Count")
plt.legend(title="Vehicle Type", bbox_to_anchor=(1, 1), loc='upper left')  
plt.savefig("bar_chart.png")  
plt.close()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=merged_data, x="Green_Light_Duration", y="Vehicle_Count", hue="Intersection", size="Vehicle_Count", palette="coolwarm", sizes=(20, 200))
plt.title("Traffic Volume vs Green Light Duration at Intersections")
plt.xlabel("Green Light Duration (Seconds)")
plt.ylabel("Total Vehicle Count")
plt.legend(title="Intersection", bbox_to_anchor=(1.05, 1), loc='upper left')  
plt.savefig("scatterplot.png", bbox_inches="tight")
plt.close()