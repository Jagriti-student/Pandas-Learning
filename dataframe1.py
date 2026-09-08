import pandas as pd

# Dictionary containing student data
students = {

    "Name": ["Jagriti", "Diksha", "Divya", "Shashwat", "Vanshika"],

    "Age": [19, 18, 16, 14, 14],

    "Marks": [100, 98, 97, 96, 95]
}

# pd.DataFrame() -> Creates a 2D tabular DataFrame
df = pd.DataFrame(students)

print("2D data is : \n", df)


# df.head() -> Shows first 5 rows
print("Head of the dataframe is : \n", df.head())

# df.tail() -> Shows last 5 rows
print("Tail of the dataframe is : \n", df.tail())

# df.tail(n) -> Shows last n rows
print("Tail of the dataframe is : \n", df.tail(2))


# df.shape -> Returns (number of rows, number of columns)
print("Shape of the dataframe is : \n", df.shape)

# df.size -> Returns total number of elements
print("Size of the dataframe is : \n", df.size)

# df.describe() -> Shows statistical summary of numerical columns
print("Description of the dataframe is : \n", df.describe())

# df.info() -> Shows DataFrame information and data types
print("Information of the dataframe is : \n", df.info())

# df.index -> Returns row index labels
print("Index of the dataframe is : \n", df.index)

# df.columns -> Returns column names
print("Columns of the dataframe is : \n", df.columns)

# df.dtypes -> Returns data type of each column
print("DataTypes of the dataframe is : \n", df.dtypes)


# Select multiple columns
print(df[["Name", "Age"]])


# loc[] -> Selects data using row/column labels
print(df.loc[0])

print(df.loc[0:3])

print(df.loc[0:2, ["Name", "Marks"]])


# iloc[] -> Selects data using row/column positions
print(df.iloc[0])

print(df.iloc[0:3])

print(df.iloc[0:3, 0:2])


# Filtering -> Select rows based on conditions
print(df[df["Marks"] > 96])


# & -> AND condition
print(df[(df["Marks"] > 96) & (df["Age"] > 16)])


# | -> OR condition
print(df[(df["Marks"] > 96) | (df["Age"] == 20)])


# ~ -> NOT condition
print(df[~(df["Age"] == 19)])


# Add a new column
df["Grade"] = ["B", "A", "C", "A", "A"]

print(df)


# Create Bonus column using Marks
df["Bonus"] = df["Marks"] + 5

print(df)


# Update all Marks values
df["Marks"] = df["Marks"] + 5

print(df)


# loc with condition -> Updates values matching condition
df.loc[df["Marks"] < 102, "Marks"] = 80

print(df)


# drop() -> Removes a column (temporary)
df6 = df.drop("Grade", axis=1)

print(df6)


# inplace=True -> Permanently modifies DataFrame
df.drop("Grade", axis=1, inplace=True)

print(df)


# Remove multiple columns
df7 = df.drop(["Age", "Marks"], axis=1)

print(df7)

print(df)


# drop(index) -> Removes row by index
df8 = df.drop(0)

print(df8)


# rename() -> Renames column names
df.rename(columns={

    "Name": "Student_Name",

    "Marks": "Score"

}, inplace=True)

print(df)



# DataFrame with missing values
df_new = pd.DataFrame({

    "Name": ["Alice", "Bob", None, "David"],

    "Age": [20, None, 22, 21],

    "Marks": [90, 85, None, 95]
})


# isnull() -> Checks missing values (True/False)
print(df_new.isnull())


# isnull().sum() -> Counts missing values in each column
print(df_new.isnull().sum())


# isna().sum() -> Counts NaN values in each column
print(df_new.isna().sum())


# dropna() -> Removes rows containing missing values
print(df_new.dropna())


# fillna(0) -> Replaces missing values with 0
print(df_new.fillna(0))


# fillna(mean) -> Fills missing Age with average Age
df_new["Age"] = df_new["Age"].fillna(df_new["Age"].mean())
print("\nAfter Filling Missing Age with Mean:\n", df_new)


# fillna(mean) -> Fills missing Marks with average Marks
df_new["Marks"] = df_new["Marks"].fillna(df_new["Marks"].mean())
print("\nAfter Filling Missing Marks with Mean:\n", df_new)


# fillna(value) -> Replaces missing Name with "Unknown"
df_new["Name"] = df_new["Name"].fillna("Unknown")
print("\nAfter Filling Missing Name:\n", df_new)


# Data for forward/backward fill
data = {

    "Name": ["Jagriti", None, None, "Diksha", None],

    "Marks": [95, None, 90, None, None]
}

# Creates a new DataFrame
dfs_test = pd.DataFrame(data)


print(dfs_test)


# ffill() -> Fills missing values using previous value
print(dfs_test.ffill())


# bfill() -> Fills missing values using next available value
print(dfs_test.bfill())


# duplicated() -> Identifies duplicate rows (True/False)
print(dfs_test.duplicated())


# duplicated().sum() -> Counts duplicate rows
print(dfs_test.duplicated().sum())


# drop_duplicates() -> Removes duplicate rows
print(dfs_test.drop_duplicates())


# drop_duplicates(subset) -> Removes duplicates based on specific column
print(dfs_test.drop_duplicates(subset="Name"))


print(df)


# sort_values() -> Sorts data in ascending order by default
print(df.sort_values("Score"))


# ascending=False -> Sorts data in descending order
print(df.sort_values("Score", ascending=False))


# Sorts multiple columns with different sorting orders
print(df.sort_values(

    ["Age", "Score"],

    ascending=[True, False]

))


# value_counts() -> Counts frequency of unique values
print(df["Age"].value_counts())


# value_counts(normalize=True) -> Returns percentage/proportion of values
print(df["Age"].value_counts(normalize=True))

