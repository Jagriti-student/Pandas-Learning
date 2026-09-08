import pandas as pd
# Create a dictionary containing names and dates
data = {
    "Name": ["Jagriti", "Diksha", "Divya", "Vanshika", "Sita"],
    "Date": [
        "2026-09-08",
        "2025-01-15",
        "2024-12-25",
        "2026-03-10",
        "2023-07-01"
    ]
}

# pd.DataFrame() creates a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# pd.to_datetime() converts Date column into datetime format
df["Date"] = pd.to_datetime(df["Date"])
print(df)

# .dt.year extracts year from the Date column
df["Year"] = df["Date"].dt.year
print(df)

# .dt.month extracts month from the Date column
df["Month"] = df["Date"].dt.month
print(df)

# .dt.day extracts day from the Date column
df["Day"] = df["Date"].dt.day
print(df)

# .dt.day_name() extracts the name of the day
df["Day_Name"] = df["Date"].dt.day_name()
print(df)


# Create another dictionary for datatype operations
data1 = {
    "Name": ["Jagriti", "Diksha", "Divya", "Vanshika"],
    "Age": ["19", "18", "17", "16"],
    "Marks": ["95", "98", "92", "96"]
}

# Create DataFrame
df1 = pd.DataFrame(data1)
print(df1)

# .dtypes checks the datatype of each column
print(df1.dtypes)

# .astype(int) converts Age column from string to integer
df1["Age"] = df1["Age"].astype(int)
print(df1)

# .astype() converts multiple columns into specified datatypes
df1 = df1.astype({
    "Age": "int",
    "Marks": "int"
})
print(df1)

# Check datatypes after conversion
print(df1.dtypes)

# .set_index() sets Name column as the DataFrame index
# inplace=True makes the change permanent
df1.set_index("Name",inplace=True)
print(df1)

# .reset_index() converts the index back into a normal column
print(df1.reset_index())

# Filter rows where Marks are greater than 94
print(df1[df1["Marks"] > 94])

# .query() filters data using a condition
print(df1.query("Marks > 94"))

# Query with AND condition: both conditions must be True
print(df1.query("Marks > 94 and Age > 16"))

# Query with OR condition: at least one condition must be True
print(df1.query("Marks > 94 or Age > 16"))

# Query rows where Age is equal to 19
print(df1.query("Age == 19"))

# Query rows where Age is not equal to 19
print(df1.query("Age != 19"))


# Create DataFrame for Pivot Table and Crosstab
df2 = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Gender": ["Male", "Female", "Male", "Female"],
    "Salary": [50000, 60000, 40000, 45000]
})
print(df2)

# pd.pivot_table() summarizes data based on rows and columns
# aggfunc="mean" calculates the average salary
pivot=pd.pivot_table(
    df2,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)
print(pivot)

# pd.crosstab() creates a frequency table between two columns
cross=pd.crosstab(
    df2["Department"],
    df2["Gender"]
)
print(cross)