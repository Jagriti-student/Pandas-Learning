import pandas as pd

# Create a dictionary
data = {
    "Name": ["Jagriti", "DIKSHA", "divya", "Vanshika", "   Sita"],
    "Address": [
        "Mumbai",
        "Thailand",
        "Punjab",
        "Goa",
        "Haryana"
    ]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Print original DataFrame
print("Original DataFrame:")
print(df)


# 1. str.upper()
# Converts all characters in the Name column to uppercase
print("\nUppercase:")
print(df["Name"].str.upper())


# 2. str.lower()
# Converts all characters in the Name column to lowercase
print("\nLowercase:")
print(df["Name"].str.lower())


# 3. str.title()
# Converts the first letter of each word to uppercase
print("\nTitle Case:")
print(df["Name"].str.title())


# 4. str.len()
# Returns the length (number of characters) of each string
print("\nString Length:")
print(df["Name"].str.len())


# 5. str.strip()
# Removes extra spaces from the beginning and end of strings
print("\nRemove Extra Spaces:")
print(df["Name"].str.strip())


# 6. str.contains()
# Checks whether a specific text exists in each string
print("\nCheck if 'divya' exists:")
print(df["Name"].str.contains("divya"))


# 7. str.replace()
# Replaces a specific substring with another substring
print("\nReplace 'divya' with 'Diya':")
print(df["Name"].str.replace("divya", "Diya"))


# 8. str.split()
# Splits each string into a list based on the given separator
print("\nSplit Strings:")
print(df["Name"].str.split(" "))