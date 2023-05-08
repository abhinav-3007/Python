import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns=150
df = pd.read_csv(r"C:\Users\Simplotel\Downloads\market_fact.csv")

plt.figure()

plt.subplot(1,2,1)
plt.boxplot(df["Sales"])
plt.title("Sales")

plt.subplot(1,2,2)
plt.boxplot(df["Sales"])
plt.title("Sales2")
plt.yscale("log")

plt.show()
