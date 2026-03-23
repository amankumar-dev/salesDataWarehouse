import pandas as pd
from db import conn

# Dataframe of customer data
custDf=pd.read_csv(r'D:\Aman\aman.code\PostgreSQL\Sales_Data_Warehouse_Project\data\customers.csv')

# Dataframe of products data
prodDf=pd.read_csv(r'D:\Aman\aman.code\PostgreSQL\Sales_Data_Warehouse_Project\data\products.csv')

# Dataframe of sales data
salesDf=pd.read_csv(r'D:\Aman\aman.code\PostgreSQL\Sales_Data_Warehouse_Project\data\sales_raw.csv')

# Dataframe of stores data
storeDf=pd.read_csv(r'D:\Aman\aman.code\PostgreSQL\Sales_Data_Warehouse_Project\data\stores.csv')

# Standarize custDf 
bussiness_key=['email']         # Rule fix kia match krney ke liye uniqueness
custDf['customer_name']=custDf['customer_name'].str.title()
custDf['email']=custDf['email'].str.lower()         # Text normalize kia duplicate check krney ke liye
custDf['city']=custDf['city'].str.title()
custDf['master_id']=(custDf.groupby(bussiness_key)['customer_id'].transform('min'))             # Email ke basis pr group bnaya aur min value se change kr dia
id_mapping=dict(custDf[custDf['customer_id']!=custDf['master_id']][['customer_id','master_id']].values)     # Un rows ko lia jishka custId change hua hai aur ushey fir masterid ke saath map kr dia
custDf=custDf.drop_duplicates(subset=bussiness_key,keep='first')                         # Removing duplicates on the basis of email column only
custDf=custDf.drop(columns=['customer_id'])

# Standarize prodDf
prodDf=prodDf[['product_name','category','cost_price','unit_price']]
prodDf['product_name']=prodDf['product_name'].str.title()
prodDf['category']=prodDf['category'].str.title()
prodDf['cost_price']=pd.to_numeric(prodDf['cost_price'],errors='coerce')        # Convert non integer into int and if can't then fill null
prodDf.loc[prodDf['cost_price']<0,'cost_price']=abs(prodDf['cost_price'])       # Handling negative values
prodDf['unit_price']=pd.to_numeric(prodDf['unit_price'],errors='coerce')        
prodDf.loc[prodDf['unit_price']<0,'unit_price']=abs(prodDf['unit_price'])
prodDf = prodDf.dropna(subset=['cost_price','unit_price'])
prodDf=prodDf.drop_duplicates(keep='first')

# Standarize storeDf
storeDf=storeDf[['store_name','region']]
storeDf.loc[storeDf['store_name'].str.contains("croma"),'store_name'] = "Tata Croma"        # Fixing fuzzy text
storeDf['store_name'] = storeDf['store_name'].str.strip().str.lower()          
storeDf['region'] = storeDf['region'].str.strip().str.lower()

# Standarize salesDf
salesDf['order_date']=pd.to_datetime(salesDf['order_date'])             # Converting normal column into datetime column
salesDf['customer_id']=salesDf['customer_id'].replace(id_mapping)       # Jo jo custId change hua hai ushey sales order mai bhi change kr rahey hai 
salesDf=salesDf.drop(columns=['order_id'])
salesDf = salesDf.dropna(subset=['customer_id','product_id','store_id'])
salesDf['revenue'] = salesDf['quantity'] * salesDf['unit_price']            # Calculating revenue because not trust in csv
salesDf['cost_amount'] = salesDf['quantity'] * salesDf['cost_price']        # Calculating cost amount 
salesDf['profit'] = salesDf['revenue'] - salesDf['cost_amount']             # Calculating profit
cust_table_df = pd.read_sql("SELECT * FROM cust_table", conn)             # Read all customer detail with surrogate key
factDf = salesDf.merge(
    cust_table_df,
    left_on='customer_id',
    right_on='source_custid',
    how='inner'
)
factDf = factDf[['custid','product_id','store_id','quantity','unit_price','cost_price','revenue','cost_amount','profit','order_date']]