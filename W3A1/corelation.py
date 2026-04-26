import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("age_networth.csv")

#print data
print(data)

# Calculate correlation
correlation = data["Age"].corr(data["Net Worth"])
print("Correlation:", correlation)

# plot
plt.figure()
plt.scatter(data["Age"], data["Net Worth"])
plt.xlabel("Age")
plt.ylabel("Net Worth")
plt.title("Age vs Net Worth")

# Add regression line
x = data["Age"]
y = data["Net Worth"]

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.show()