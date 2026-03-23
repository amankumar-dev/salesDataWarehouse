from db import conn,cursor

# Loading dim tables
def load_cust(custDf):    
    # Calculating conditions
    total_row=len(custDf)
    dup_row=custDf.duplicated().sum()
    null_val=custDf.isnull().sum().sum()
    
    # Printing details
    print(f'{'='*20} Customer details {'='*20}')
    print('Total rows: ',total_row)
    print('Duplicated rows: ',dup_row)
    print('Null values: ',null_val)
    
def load_prod(prodDf):
    # Calculating conditions
    total_row=len(prodDf)
    dup_row=prodDf.duplicated().sum()
    null_val=prodDf.isnull().sum().sum()
    
    # Printing details
    print(f'{'='*20} Product details {'='*20}')
    print('Total rows: ',total_row)
    print('Duplicated rows: ',dup_row)
    print('Null values: ',null_val)
    
def load_store(storeDf):
    # Calculating conditions
    total_row=len(storeDf)
    dup_row=storeDf.duplicated().sum()
    null_val=storeDf.isnull().sum().sum()
    
    # Printing details
    print(f'{'='*20} Store details {'='*20}')
    print('Total rows: ',total_row)
    print('Duplicated rows: ',dup_row)
    print('Null values: ',null_val)
    
def load_order(salesDf):
    # Calculating conditions
    total_row=len(salesDf)
    dup_row=salesDf.duplicated().sum()
    null_val=salesDf.isnull().sum().sum()
    
    # Printing details
    print(f'{'='*20} Sales details {'='*20}')
    print('Total rows: ',total_row)
    print('Duplicated rows: ',dup_row)
    print('Null values: ',null_val)
    
# Loading total revenue
def total_revenue():
    with conn:
        try:
            cursor.execute('''SELECT SUM(revenue) FROM order_table;''')
            result=cursor.fetchone()[0]
            return result
        except Exception as e:
            print('Something went wrong ',e)

# Loading revenue by month
def month_revenue():
    with conn:
        try:
            cursor.execute('''SELECT 
                                EXTRACT(YEAR FROM order_date)::INT AS year,
                                EXTRACT(MONTH FROM order_date)::INT AS month,
                                SUM(revenue) AS total_revenue
                                FROM order_table
                            GROUP BY year,month
                            ORDER BY year,month;
                           ''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print('Something went wrong: ',e)

# Loading revenue by region
def region_revenue():
    with conn:
        try:
            cursor.execute('''SELECT
                                s.region,SUM(o.revenue)
                                AS total_revenue
                                FROM order_table o
                                JOIN store_table s
                                ON s.storeid=o.storeid
                                GROUP BY s.region
                                ORDER BY total_revenue DESC;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print("Can't fetch data")

