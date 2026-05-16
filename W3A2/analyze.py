import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("messy_dataset.csv")

print("Original Dataset:\n", df.head())

# ----------------------------
# 🧹 DATA CLEANING
# ----------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Fix Age column (convert text to numeric)
df['Age'] = df['Age'].replace('thirty-eight', 38)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Convert Salary to numeric
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Convert Join Date to datetime (optional but good practice)
df['Join Date'] = pd.to_datetime(df['Join Date'], errors='coerce')

# Handle missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print("\nCleaned Dataset:\n", df.head())

# ----------------------------
# 📊 CORRELATION HEATMAP
# ----------------------------

# Select only numeric columns
numeric_df = df.select_dtypes(include=['number'])

print("\nCorrelation Matrix:\n", numeric_df.corr())

# Plot heatmap
plt.figure(figsize=(8,5))
sns.heatmap(numeric_df.corr(method='pearson'), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap (Pearson)")
plt.tight_layout()
plt.show()

# ----------------------------
# 🚨 OUTLIER DETECTION
# ----------------------------

plt.figure(figsize=(8,5))
numeric_df.boxplot()
plt.title("Outlier Detection using Boxplot")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()