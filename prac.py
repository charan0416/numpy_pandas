import pandas as pd
import matplotlib.pyplot as plt

# Creating the initial DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Chris'],
        'Age': [28, 24, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Accessing individual columns
print("\n'Name' Column:")
print(df['Name'])
print("\n'Name' and 'Age' Columns:")
print(df[['Name', 'Age']])

# Accessing rows using iloc and loc
print("\nRow at index 1:")
print(df.iloc[1])  # Row at index 1
print("\nRows from index 0 to 1:")
print(df.iloc[0:2])  # Rows from index 0 to 1 (inclusive)
print("\nRow at index 1 using loc:")
print(df.loc[1])  # Row at index 1 (same as iloc[1])

# Adding a new column 'Salary'
df['Salary'] = [50000, 60000, 70000, 80000]
print("\nAfter adding 'Salary' Column:")
print(df)

# Dropping the 'Salary' column
df.drop('Salary', axis=1, inplace=True)
print("\nAfter dropping 'Salary' Column:")
print(df)

# Modifying the 'Age' column
df['Age'] = df['Age'] + 2
print("\nAfter increasing 'Age' by 2:")
print(df)

# Creating a new column 'New_Salary'
df['New_Salary'] = df['Age'] * 1000
print("\nAfter adding 'New_Salary' Column:")
print(df)

# Checking for missing values
print("\nChecking for missing values:")
print(df.isnull())
print("\nSum of missing values per column:")
print(df.isnull().sum())

# Handling missing values in 'Age' (if any)
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Dropping rows with missing values
df.dropna(inplace=True)

# Aggregating the data by 'City' and calculating mean, max, and min for 'Age'
agg = df.groupby('City').agg({'Age': ['mean', 'max', 'min']})
print("\nAggregated data by 'City':")
print(agg)

# Merging two DataFrames (df1 and df2)
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['John', 'Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Age': [28, 24, 22]})
merged = pd.merge(df1, df2, on='ID')
print("\nMerged DataFrame (df1 + df2):")
print(merged)

# Concatenating two DataFrames (df1 and df2)
df_concat = pd.concat([df1, df2], axis=0)
print("\nConcatenated DataFrame (df1 + df2):")
print(df_concat)

# Pivot table to summarize 'Amount' by 'Date' and 'Category'
df = pd.DataFrame({
    'Date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Amount': [100, 200, 150, 250]
})
pivot = df.pivot_table(values='Amount', index='Date', columns='Category', aggfunc='sum')
print("\nPivot Table by 'Date' and 'Category':")
print(pivot)

# Applying a function to modify 'Age' column and calculating rolling average
print("\nColumns before applying function:", df.columns)

# Ensure the 'Age' column exists before applying the function
if 'Age' in df.columns:
    df['Age'] = df['Age'].apply(lambda x: x + 1)
else:
    print("'Age' column is missing!")

# Calculate rolling average for 'Age' column
df['Rolling_Avg'] = df['Age'].rolling(window=2).mean()
print("\nDataFrame with 'Rolling_Avg' Column:")
print(df)

# Plotting histogram of the 'Age' column
df['Age'].plot(kind='hist', bins=5)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Filtering data based on conditions (Age > 25, non-null City, and sorted by Age)
df = df[df['Age'] > 25].dropna(subset=['City']).sort_values(by='Age')
print("\nFiltered DataFrame where 'Age' > 25 and sorted by 'Age':")
print(df)
