import pandas as pd
import numpy as np

# pd.read_excel() reads data from an Excel file
df = pd.read_excel(r"C:\Users\gsasw\Desktop\data.xlsx")

print(df)

# pd.read_csv() reads data from a CSV file
df1 = pd.read_csv(r"D:\downloads\industry.csv")

print(df1)


# ---------------- DATAFRAME CREATION ----------------

data = {

    "Name": ["Jagriti", "Diksha", "Divya", "Vanshika"],

    "Age": [19, 18, 17, 16],

    "Marks": [95, 98, 92, 96]

}

# pd.DataFrame() creates a DataFrame
df = pd.DataFrame(data)

print(df)


# ---------------- SAVING FILES ----------------

# to_csv() saves the DataFrame as a CSV file
# index=False prevents saving row index
df.to_csv("output.csv", index=False)

print(df)


# ---------------- RANDOM SAMPLING ----------------

# sample() returns one random row
print(df.sample())

# sample(2) returns 2 random rows
print(df.sample(2))

# sample(frac=0.5) returns 50% random rows
print(df.sample(frac=0.5))


# ---------------- CONDITIONAL OPERATIONS ----------------

data = {

    "Name": ["Jagriti", "Diksha", "Divya", "Vanshika", "Sita"],

    "Marks": [95, 82, 65, 38, 25]

}

df_new = pd.DataFrame(data)

print("Original DataFrame:")

print(df_new)


# np.where() checks a condition and assigns values accordingly
df_new["Result"] = np.where(

    df_new["Marks"] >= 40,

    "Pass",

    "Fail"

)

print("\nUpdated DataFrame:")

print(df_new)


# Define multiple conditions for grade assignment
conditions = [

    df_new["Marks"] >= 90,

    df_new["Marks"] >= 75,

    df_new["Marks"] < 75

]

# Define values corresponding to each condition
choices = ["A", "B", "C"]


# np.select() assigns values based on multiple conditions
df_new["Grade"] = np.select(

    conditions,

    choices,

    default="Not Assigned"

)

print("\nUpdated DataFrame:")

print(df_new)



# ---------------- TRANSFORM FUNCTION ----------------

df_dept = pd.DataFrame({

    "Department": ["IT", "IT", "HR", "HR"],

    "Salary": [50000, 60000, 40000, 45000]

})

print("Original DataFrame:")

print(df_dept)


# groupby() groups data by Department
# transform("mean") calculates average while keeping the same number of rows
df_dept["Avg_Salary"] = df_dept.groupby(

    "Department"

)["Salary"].transform("mean")

print("\nAfter transform:")

print(df_dept)



# ---------------- CORRELATION ----------------

df_corr = pd.DataFrame({

    "Hours_Studied": [2, 4, 6, 8, 10],

    "Marks": [40, 55, 70, 85, 95],

    "Attendance": [60, 70, 80, 90, 95]

})

print(df_corr)


# corr() calculates the relationship between numerical columns
# numeric_only=True uses only numeric data
correlation = df_corr.corr(numeric_only=True)

print("\nCorrelation Matrix:")

print(correlation)



# ---------------- MELT FUNCTION ----------------

df_stu = pd.DataFrame({

    "Name": ["Alice", "Bob"],

    "Math": [90, 85],

    "Science": [85, 88]

})

print("Original DataFrame:")

print(df_stu)


# pd.melt() converts wide-format data into long-format data
# id_vars keeps the specified column unchanged
# value_vars converts selected columns into rows
melted = pd.melt(

    df_stu,

    id_vars=["Name"],

    value_vars=["Math", "Science"]

)

print(melted)

