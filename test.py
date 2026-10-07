import pandas as pd

data={
    'Name':['Bhanu','Ankur','Rahul'],
    'Age':[24,23,22],
    'Salary':[50000,60000,40000]
}

df=pd.DataFrame(data)
print(df.head()) #To print/Find the Top Rows of the Data.

print(df.tail()) #To print/Find the last Rows of the Data.

print(df.shape) # To print the total of rows and columns.

print(df.columns) # To print the columns Name.

df.rename(columns={'Salary':'Monthly_Salary'},inplace=True) # rename the value 2. inplace we used because when we dont use the
                                                           #inplace it will not permanently change the value to change the value permanent we use inplace.
print(df)

print(df.info()) # to print the info of data frame

print(df.describe()) # to describe the data frame 2. it shows the high level statistical summary of numerical values