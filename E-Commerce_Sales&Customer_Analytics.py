import pandas as pd

#Creating sample datasets 
#---------------1st dataset of orders----------------
orders = {
    "Order_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "Customer_ID": ["C01","C02","C03","C01","C04","C05","C02","C06","C03","C07"],
    "Product": ["Laptop","Phone","Headphones","Laptop","Mouse",
                "Keyboard","Phone","Monitor","Headphones","Laptop"],
    "Category": ["Electronics","Electronics","Accessories","Electronics",
                 "Accessories","Accessories","Electronics","Electronics",
                 "Accessories","Electronics"],
    "Quantity": [1,2,3,1,2,1,1,2,2,1],
    "Price": [60000,25000,2000,60000,800,1500,25000,18000,2000,60000],
    "Order_Date": ["2026-01-05","2026-01-08","2026-01-10","2026-01-15",
                   "2026-01-20","2026-02-01","2026-02-05","2026-02-10",
                   "2026-02-15","2026-03-01"]
}

#------------------2nd dataset for customers----------------
customers = {
    "Customer_ID": ["C01","C02","C03","C04","C05","C06","C07"],
    "Name": ["Jagriti","Diksha","Divya","Shashwat","Vanshika","Riya","Ananya"],
    "Age": [20,21,19,22,20,24,23],
    "City": ["Hisar","Delhi","Mumbai","Delhi","Hisar","Jaipur","Chandigarh"]
}

#--------------------3rd dataset for products-----------------
products = {
    "Product": ["Laptop","Phone","Headphones","Mouse","Keyboard","Monitor"],
    "Category": ["Electronics","Electronics","Accessories",
                 "Accessories","Accessories","Electronics"],
    "Supplier": ["Dell","Samsung","Boat","Logitech","HP","LG"],
    "Cost_Price": [45000,18000,1200,500,900,14000]
}

#-------------------4th dataset for payments-----------------
payments = {
    "Order_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    "Payment_Mode": ["UPI","Card","UPI","Card","Cash",
                     "UPI","Card","UPI","Cash","Card"],
    "Status": ["Paid","Paid","Paid","Paid","Paid",
               "Paid","Pending","Paid","Paid","Paid"]
}

#---------------------PART 1 — DataFrame Basics-----------------
df=pd.DataFrame(orders)
print("Orders dataframe is : \n",df)

df1=pd.DataFrame(customers)
print("Customers dataframe is \n: ",df1)

df2=pd.DataFrame(products)
print("Products Dataframe is : \n",df2)

df3=pd.DataFrame(payments)
print("payments Dataframe is : \n",df3)

print("First 5 rows of orders dataset is : \n",df.head())

print("Last 5 rows of orders dataset is : \n",df.tail())

print("Shape of the orders dataset is : \n",df.shape)

print("Size of the orders dataset is : \n",df.size)

print("DataTypes of the orders dataset is : ",df.dtypes)

print("Information about the orders dataset is : ",df.info())

print("Statistical Information about orders dataset is : \n",df.describe())

print("Index fucntion is : ",df.index)

print("columns function is : ",df.columns)

#----------------PART 2 — Selection----------------
print("Products are : \n",df[["Product"]])

print("Selected products their quantities and prices are : \n",df[["Product","Quantity","Price"]])

print("First 3 rows of orders datset : \n",df.loc[1:3])

print("First 3 rows of orders datset : \n",df.iloc[0:3])

print("2-5 rows and specific column : \n",df.loc[2:5,["Product","Price"]])

#------------------PART 3 — Filtering------------------------
print("Orders where Price greater than 20000 : \n",df[df["Price"]>20000])

print("Orders where Quantity greater than and equal to 2 : \n",df[df["Quantity"]>=2])

print("Electronic orders : \n",df[df["Category"]=="Electronics"])

print("Orders where price is greater than 20000 and quantity is greater than or equal to 2 is : ",df[(df["Price"]>20000) & (df["Quantity"]>=2)])

print("Orders where product is Laptop or phone : \n",df[(df["Product"]=="Laptop") | (df["Product"]=="Phone")])

print("Orders where price is between 2000 to 30000 : \n",df[df["Price"].between(2000,30000)])

print("Orders that are not electronics : \n",df[~(df["Category"]=="Electronics")])


#--------------PART 4 — Create New Columns-----------------
df["Revenue"]=df["Quantity"]*df["Price"]
print("Revenue Column is : \n",df)

df["Profit"]=df["Revenue"]-(df["Quantity"]*df2["Cost_Price"])
print("Profit is : \n",df)

#----------------------------PART 5 — DateTime-------------------

df["Order_Date"]=pd.to_datetime(df["Order_Date"])
df["Year"]=df["Order_Date"].dt.year
print("Year of the orders : \n",df)

df["Month"]=df["Order_Date"].dt.month
print("Month of the orders : \n",df)

df["Month_Name"]=df["Order_Date"].dt.month_name()
print("Month name for orders : \n",df)

df["Day"]=df["Order_Date"].dt.day
print("Day of the order : \n",df)

df["Day_Name"]=df["Order_Date"].dt.day_name()
print("Name of the day for order : \n",df)

#------------------PART 6 — Missing Data------------------
'''print("Check any record id null or not : \n",df.isnull())

print("Check for is null and count : \n",df.isnull().sum())

print("Check for NaN Values : \n",df.isna())

print("Drop NaN values : \n",df.dropna())

print("Fill the NaN values : \n",df.fillna(0))'''

#--------------------PART 7 — Duplicates------------------
print("Check that values are duplicated or not : \n",df.duplicated())

print("Check that values are duplicated or not and sum of it : \n",df.duplicated().sum())

print("For drop the duplicate values : \n",df.drop_duplicates())

#-------------------------PART 8 — String Operations---------------------
print("String lowercase : \n",df["Product"].str.lower())

print("String uppercase : \n",df["Product"].str.upper())

print("String Title: \n",df["Product"].str.title())

print("Length of String : \n",df["Product"].str.len())

print("String Contains an element : \n",df1["Name"].str.contains("Divya"))

print("String startswith : \n",df["Product"].str.startswith("Laptop"))

print("String endswith : \n",df["Product"].str.endswith("Headphones"))

print("String strip is : \n",df["Product"].str.strip("  "))

#-----------------------PART 9 — Statistics------------------
print("Total revenue is : \n",df["Revenue"].sum())

print("Average revenue is : \n",df["Revenue"].mean())

