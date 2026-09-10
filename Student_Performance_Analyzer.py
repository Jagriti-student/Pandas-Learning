import pandas as pd

students = {
    "Name": ["Jagriti", "Diksha", "Divya", "Shashwat", "Vanshika"],
    "Age": [19, 18, 16, 14, 14],
    "Maths": [95, 88, 92, 76, 89],
    "Science": [90, 85, 95, 80, 91],
    "English": [88, 92, 87, 75, 90]
}

df = pd.DataFrame(students)

print("Student Data:")
print(df)

# Total Marks
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)

# Average Marks
df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

# Grade
def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(grade)

# Pass / Fail
df["Result"] = (
    (df["Maths"] >= 40) &
    (df["Science"] >= 40) &
    (df["English"] >= 40)
).map({True: "Pass", False: "Fail"})

print("\nFinal Student Data:")
print(df)

# Top Student
top_student = df.loc[df["Total"].idxmax()]
print("\nTop Student:")
print(top_student)

# Lowest Student
lowest_student = df.loc[df["Total"].idxmin()]
print("\nLowest Student:")
print(lowest_student)

# Overall Average
overall_average = df["Average"].mean()
print("\nOverall Average:", overall_average)

# Students Above Average
above_average = df[df["Average"] > overall_average]
print("\nStudents Above Average:")
print(above_average)

# Sort Students by Total Marks
sorted_students = df.sort_values("Total", ascending=False)
print("\nStudents Sorted by Total Marks:")
print(sorted_students)

# Students Between Ages 14 and 18
age_students = df[df["Age"].between(14, 18)]
print("\nStudents Between Age 14 and 18:")
print(age_students)

# Subject-wise Average
subject_average = df[["Maths", "Science", "English"]].mean()
print("\nSubject-wise Average:")
print(subject_average)