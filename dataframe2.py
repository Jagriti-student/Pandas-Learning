import pandas as pd


# Dictionary containing student data
Demo = {

    "Name": ["Jagriti", "Diksha", "Divya", "Vanshika", "Sita"],

    "Age": [19, 18, 17, 16, 15],

    "Marks": [100, 95, 98, 96, 84]

}

# pd.DataFrame() -> Creates a table from dictionary
df = pd.DataFrame(Demo)

print(df)


# unique() -> Shows all unique values
print(df["Age"].unique())


# nunique() -> Counts unique values
print(df["Age"].nunique())


# sum() -> Adds all values
print("Sum is : ", df["Marks"].sum())


# mean() -> Calculates average
print("Mean is : ", df["Marks"].mean())


# median() -> Finds middle value
print("Median is : ", df["Marks"].median())


# std() -> Calculates data spread from mean
print("Standard Deviation is : ", df["Marks"].std())


# var() -> Calculates data variation
print("Variance is : ", df["Marks"].var())


# mode() -> Finds most frequent value
print("Mode is : ", df["Marks"].mode())


# min() -> Finds smallest value
print("Minimum is : ", df["Marks"].min())


# max() -> Finds largest value
print("Maximum is : ", df["Marks"].max())


# count() -> Counts non-missing values
print("Count is : ", df["Marks"].count())


# mean() -> Calculates average of multiple columns
print(df[["Age", "Marks"]].mean())


# Department employee data
dept = pd.DataFrame({

    "Department": ["IT", "HR", "IT", "HR"],

    "Name": ["A", "B", "C", "D"],

    "Salary": [50000, 40000, 60000, 45000]

})


# groupby() -> Groups data by Department
# mean() -> Finds average salary of each department
print(dept.groupby("Department")["Salary"].mean())


# agg() -> Performs multiple calculations at once
print(dept.groupby("Department")["Salary"].agg(

    ["mean", "sum", "max", "min"]

))


# agg() -> Applies functions to selected column
print(dept.groupby("Department").agg({

    "Salary": ["mean", "max"],

}))


# First DataFrame
df1 = pd.DataFrame({

    "ID": [1, 2, 3],

    "Name": ["Alice", "Bob", "Charlie"]

})


# Second DataFrame
df2 = pd.DataFrame({

    "ID": [1, 2, 3, 4],

    "Marks": [90, 85, 95, 90]

})


# merge() -> Combines DataFrames using common column
# Default inner join -> Keeps only matching IDs
print(pd.merge(df1, df2, on="ID"))


# Left join -> Keeps all rows from df1
print(pd.merge(df1, df2, on="ID", how="left"))


# Right join -> Keeps all rows from df2
print(pd.merge(df1, df2, on="ID", how="right"))


# Outer join -> Keeps all rows from both DataFrames
print(pd.merge(df1, df2, on="ID", how="outer"))


# DataFrames for concatenation
df3 = pd.DataFrame({

    "Name": ["Alice", "Bob"]

})

df4 = pd.DataFrame({

    "Name": ["Charlie", "David"]

})


# concat() -> Combines DataFrames vertically (row-wise)
print(pd.concat([df3, df4]))


# concat(axis=1) -> Combines DataFrames horizontally (column-wise)
print(pd.concat([df1, df2], axis=1))


# apply() -> Applies a function to every value
# lambda -> Small one-line function
# Adds 5 to every Marks value and saves the changes
df["Marks"] = df["Marks"].apply(lambda x: x + 5)

print(df)


# Function -> Assigns grade based on marks
def grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    else:
        return "C"


# apply() -> Applies grade function to every Marks value
df["Grade"] = df["Marks"].apply(grade)

print(df)


# map() -> Maps specific values to new values
df["Grade"] = df["Marks"].map({

    90: "A",

    85: "B",

    98: "C",

    100: "A"

})

print(df)


# DataFrame containing gender values
df7 = pd.DataFrame({

    "Name": ["Sita", "Gita", "Teena", "Payal", "Golu"],

    "Gender": ['F', 'F', 'F', 'F', 'M']

})


# replace() -> Replaces a specific value
print(df7.replace("M", "Male"))


# replace() -> Replaces multiple values using dictionary
print(df7.replace({

    "M": "Male",

    "F": "Female"

}))

