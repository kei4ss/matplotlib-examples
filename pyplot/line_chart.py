import matplotlib.pyplot as plt
import pandas as pd

# load data
df = pd.read_csv("./../datasets/bedtime_screentime_sleep_debt.csv")
collumns = df[["age", "total_sleep_hours"]].iloc[0: 50: 3]
collumns = collumns.sort_values(by="age")
age = collumns["age"]
total_sleep_hours = collumns["total_sleep_hours"]

# Create line chart, x=age | y=total sleep hours
plt.plot(
    age,
    total_sleep_hours,
    color="red", #line color
    marker="o",
    linestyle="dotted"
)

plt.title("Example chart")
plt.xlabel("age")
plt.ylabel("total sleep hours")

plt.show()
