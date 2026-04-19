import pandas as pd
import glob

## combining files
files = glob.glob("PRSA_Data_*.csv")
df_list = []
for file in files:
    temp_df = pd.read_csv(file)
    df_list.append(temp_df)

df= pd.concat(df_list,ignore_index=True)

print("First five Rows:\n")
print(df.head(5))
print(df.columns)      # column names
print(df.dtypes)       # data types
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


print(df.info())