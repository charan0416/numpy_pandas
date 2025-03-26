import pandas as pd


# data = [10, 20, 30, 40, 50]
# series = pd.Series(data)
#
# print(series)



data = {'Name': ['John', 'Alice', 'Bob', 'Chris'],
        'Age': [28, 24, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

print(df)



print(df['Name'])

print(df[['Name', 'Age']])



print(df.iloc[1])

print(df.iloc[0:2])


print(df.loc[1])


df['Salary'] = [50000, 60000, 70000, 80000]
print(df)

df.drop('Salary', axis=1, inplace=True)
print(df)



df['Age'] = df['Age'] + 2


df['New_Salary'] = df['Age'] * 1000

print(df.isnull())

print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())

df.dropna(inplace=True)


agg = df.groupby('City').agg({'Age': ['mean', 'max', 'min']})
print(agg)


df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['John', 'Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Age': [28, 24, 22]})

merged = pd.merge(df1, df2, on='ID')
print(merged)



print(df.isnull())


print(df.isnull().sum())



df['Age'] = df['Age'].fillna(df['Age'].mean())

df.dropna(inplace=True)

grouped = df.groupby('City')['Age'].mean()
print(grouped)


agg = df.groupby('City').agg({'Age': ['mean', 'max', 'min']})
print(agg)


df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['John', 'Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Age': [28, 24, 22]})

merged = pd.merge(df1, df2, on='ID')
print(merged)

df_concat = pd.concat([df1, df2], axis=0)
df = pd.DataFrame({
    'Date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Category': ['A', 'B', 'A', 'B'],
    'Amount': [100, 200, 150, 250]
})

pivot = df.pivot_table(values='Amount', index='Date', columns='Category', aggfunc='sum')
print(pivot)


