import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./../datasets/bedtime_screentime_sleep_debt.csv")

jobs = set()
for job in df["occupation_type"]:
    jobs.add(job)

peopleByCategories = {
    x: int(df["occupation_type"].str.contains(x).sum()) for x in jobs
}

plt.bar(
    peopleByCategories.keys(),
    peopleByCategories.values()
)

plt.ylabel("Pessoas")
plt.xlabel("Empregos")

plt.show()
