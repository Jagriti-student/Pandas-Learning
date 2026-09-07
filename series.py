import pandas as pd

# Creates a 1D Pandas Series
d1 = pd.Series([1, 2, 3, 4, 5])

print("Linear sequence / 1D array is : \n", d1)


# Creates Series with custom index labels
d2 = pd.Series(
    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
)

print("Tabular form data : ", d2)


# Accesses value using index label
print(d2['d'])


# head() -> Shows first 5 values by default
print("Head of the series : ", d2.head())


# tail() -> Shows last 5 values by default
print("Tail of the series : ", d2.tail())


# size -> Returns total number of elements
print("Size of the series : ", d2.size)


# shape -> Returns dimensions of the Series
print("Shape of the series : ", d2.shape)


# dtype -> Returns data type of values
print("DataType of the series : ", d2.dtype)


# values -> Returns all values as an array
print("Values of the series : ", d2.values)


# index -> Returns all index labels
print("Index of the series : ", d2.index)


# sum() -> Adds all values
print("Sum of the series : ", d1.sum())


# min() -> Returns smallest value
print("Minimum of the series : ", d2.min())


# max() -> Returns largest value
print("Maximum of the series : ", d2.max())


# mean() -> Returns average of values
print("Mean of the series : ", d2.mean())


# count() -> Counts non-null values
print("Count of the series : ", d2.count())


# sort_values() -> Sorts values in ascending order
print("Sort the series in ascending order : ", d2.sort_values())


# ascending=False -> Sorts values in descending order
print("Sort the series in descending order : ", d2.sort_values(ascending=False))


# Series with unordered index labels
d3 = pd.Series(
    [30, 10, 50, 20],
    index=['c', 'a', 'd', 'b']
)

print(d3)


# sort_index() -> Sorts based on index labels in ascending order
print("Sort the index value in ascending order : ", d3.sort_index())


# ascending=False -> Sorts index labels in descending order
print("Sort the index value in descending order : ", d3.sort_index(ascending=False))


# unique() -> Returns all distinct values
print("All unique values from d2 : ", d2.unique())


# nunique() -> Returns count of distinct values
print("Count of all unique values from d2 : ", d2.nunique())


# value_counts() -> Counts frequency of each unique value
print("Count of each Unique Value : ", d2.value_counts())