# ==============================================================================
# Comprehensive Pandas Masterclass (PandasDemo)
# ==============================================================================
import pandas as pd
import numpy as np

# 1. Core Data Structures: Series & DataFrame
print("--- 1. Creating Series & DataFrame ---")
# Series: 1D labeled array
ages = pd.Series([22, 25, 29, 31], index=["Alice", "Bob", "Charlie", "Diana"], name="Age")
print("Pandas Series:\n", ages)

# DataFrame: 2D tabular structure with labeled rows and columns
data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan", "Fiona"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Salary": [75000, 52000, 82000, 95000, 48000, 91000],
    "JoinDate": ["2021-01-15", "2020-03-22", "2019-07-10", "2022-11-05", "2023-02-18", "2021-08-30"],
    "Bonus": [5000.0, np.nan, 8000.0, 10000.0, np.nan, 7500.0]  # Includes missing values
}
df = pd.DataFrame(data)

# 2. 5 Commonly Used Pandas Functions (Preserved & Working)
print("\n--- 2. Inspecting Data ---")
# 1) head() - Display the first few rows of a DataFrame
print("df.head(3):\n", df.head(3))

# 2) tail() - Display the last few rows
print("\ndf.tail(2):\n", df.tail(2))

# 3) describe() - Generate descriptive statistics of numerical columns
print("\ndf.describe():\n", df.describe())

# 4) info() - Concise summary with datatypes and non-null counts
print("\ndf.info():")
df.info()

# 5) to_datetime() - Convert argument to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
print(f"\nJoinDate converted dtype: {df['JoinDate'].dtype}")

# 3. Selection & Indexing: loc vs iloc
print("\n--- 3. Selection: loc vs iloc ---")
# loc: Label-based indexing [row_label, col_label]
print("loc (Rows 0-2, Columns 'Name' & 'Salary'):\n", df.loc[0:2, ["Name", "Salary"]])

# iloc: Integer position-based indexing [row_pos, col_pos]
print("\niloc (First 3 rows, First 3 columns):\n", df.iloc[:3, :3])

# 4. Filtering & Querying
print("\n--- 4. Filtering & Conditional Queries ---")
# Multiple conditions with & (AND), | (OR)
it_high_earners = df[(df["Department"] == "IT") & (df["Salary"] > 70000)]
print("IT employees earning > 70,000:\n", it_high_earners[["Name", "Salary"]])

# Using query() method for readable string filtering
finance_staff = df.query("Department == 'Finance' and Salary >= 90000")
print("\nFinance staff with Salary >= 90,000:\n", finance_staff[["Name", "Salary"]])

# 5. Handling Missing Data (NaN)
print("\n--- 5. Handling Missing Data ---")
print("Missing values count per column:\n", df.isna().sum())

# Filling missing values (fillna)
df_filled = df.copy()
df_filled["Bonus"] = df_filled["Bonus"].fillna(0.0)
print("\nBonus column filled with 0.0:\n", df_filled[["Name", "Bonus"]])

# 6. GroupBy & Aggregations
print("\n--- 6. GroupBy & Aggregations ---")
# groupby() - Group DataFrame by columns and calculate statistics
dept_stats = df.groupby("Department")["Salary"].agg(["count", "mean", "min", "max"])
print("Salary statistics by Department:\n", dept_stats)

# 7. Creating New Columns & Applying Functions
print("\n--- 7. Feature Engineering with apply() ---")
# Total compensation column
df_filled["TotalComp"] = df_filled["Salary"] + df_filled["Bonus"]
# Categorizing employees with custom function
df_filled["Seniority"] = df_filled["JoinDate"].apply(lambda dt: "Senior" if dt.year <= 2020 else "Junior")
print(df_filled[["Name", "Department", "TotalComp", "Seniority"]])

# 8. Sorting & Value Counts
print("\n--- 8. Sorting & Distribution ---")
print("Department counts:\n", df["Department"].value_counts())
print("\nSorted by Salary descending:\n", df_filled.sort_values(by="Salary", ascending=False)[["Name", "Salary"]])

# 9. In-Memory Export & Import Demonstration
print("\n--- 9. Export & Import Demonstration ---")
# Export DataFrame to CSV string (in-memory, no disk clutter)
csv_buffer = df_filled.to_csv(index=False)
print("Exported CSV preview (first 3 lines):")
for line in csv_buffer.strip().split("\n")[:3]:
    print("  ", line)

# Re-read back into DataFrame using read_csv
from io import StringIO
df_reloaded = pd.read_csv(StringIO(csv_buffer))
print("Successfully reloaded DataFrame with shape:", df_reloaded.shape)