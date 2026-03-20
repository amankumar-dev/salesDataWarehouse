import pandas as pd

# Dataframe of customer data
custDf=pd.read_csv(r'D:\Aman\aman.code\PostgreSQL\Sales_Data_Warehouse_Project\data\customers.csv')

# Dataframe of products data
prodDf=pd.read_csv(r'D:\Aman\aman.code\PostgreSQL\Sales_Data_Warehouse_Project\data\products.csv')

# Dataframe of sales data
salesDf=pd.read_csv(r'D:\Aman\aman.code\PostgreSQL\Sales_Data_Warehouse_Project\data\sales_raw.csv')

# Dataframe of stores data
storeDf=pd.read_csv(r'D:\Aman\aman.code\PostgreSQL\Sales_Data_Warehouse_Project\data\stores.csv')

custDf=custDf[['customer_name','email','city']]

prodDf=prodDf[['product_name','category','cost_price','unit_price']]

storeDf=storeDf[['store_name','region']]

salesDf['order_date']=pd.to_datetime(salesDf['order_date'])             # Converting normal column into datetime column
salesDf=salesDf.drop(columns=['order_id'])