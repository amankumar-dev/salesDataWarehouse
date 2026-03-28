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

# Loading revenue by category
def category_revenue():
    with conn:
        try:
            cursor.execute('''SELECT
                                p.category,SUM(revenue)
                                AS total_revenue
                                FROM order_table o
                                JOIN prod_table p
                                ON p.prodid=o.prodid
                                GROUP BY p.category
                                ORDER BY total_revenue DESC;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print("Can't collect data ",e)
            
# Loading Top 10 prod by revenue
def top_prod():
    with conn:
        try:
            cursor.execute('''SELECT
                                p.prodname,SUM(revenue)
                                AS total_revenue
                                FROM order_table o
                                JOIN prod_table p
                                ON p.prodid=o.prodid
                                GROUP BY p.prodname
                                ORDER BY total_revenue DESC
                                LIMIT 10;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print("Can't fetched data ",e)

# Getting least selling product
def least_sell():
    with conn:
        try:
            cursor.execute('''SELECT
                                p.prodname,SUM(quantity)
                                AS total_quantity
                                FROM order_table o
                                JOIN prod_table p
                                ON p.prodid=o.prodid
                                GROUP BY p.prodname
                                ORDER BY total_quantity
                                LIMIT 1;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print("Can't get data ",e)

# Getting profit margin
def profit_margin():
    with conn:
        try:
            cursor.execute('''SELECT
                                p.prodname,
                                ROUND((SUM(o.profit)::NUMERIC/NULLIF(SUM(o.revenue),0))*100,2)
                                as profit_margin
                                FROM order_table o
                                JOIN prod_table p
                                ON p.prodid=o.prodid
                                GROUP BY p.prodname
                                ORDER BY profit_margin desc;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print("Can't calculate ",e)

# Category performance
def cat_perform():
    with conn:
        try:
            cursor.execute('''SELECT
                                p.category,
                                SUM(o.revenue) AS total_revenue,
                                SUM(profit) AS total_profit,
                                ROUND((SUM(o.profit)::NUMERIC/NULLIF(SUM(o.revenue),0))*100,2)
                                FROM order_table o
                                JOIN prod_table p
                                ON p.prodid=o.prodid
                                GROUP BY p.category
                                ORDER BY total_revenue DESC;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print("Can't calculate ",e)
            
# Top Customer by Revenue
def top_cust():
    with conn:
        try:
            cursor.execute('''SELECT
                                c.custid,
                                c.custname,
                                SUM(o.revenue) AS total_revenue
                                FROM order_table o
                                JOIN cust_table c
                                ON c.custid=o.custid
                                GROUP BY c.custid,c.custname
                                ORDER BY total_revenue DESC;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print("Can't fetch ",e)

# Repeat Customer in sales
def rep_cust():
    with conn:
        try:
            cursor.execute('''SELECT
                                c.custname,
                                c.email,
                                COUNT(*) AS repeat_cust
                                FROM order_table o
                                JOIN cust_table c
                                ON c.custid=o.custid
                                GROUP BY c.custname,c.email
                                HAVING COUNT(*)>1
                                ORDER BY repeat_cust DESC;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            
# Customer count by region
def cust_count_reg():
    with conn:
        try:
            cursor.execute('''SELECT
                                s.region,
                                COUNT(*) AS reg_cust
                                FROM cust_table c
                                JOIN store_table s
                                ON s.city=c.city
                                GROUP BY s.region
                                HAVING COUNT(*)>1
                                ORDER BY reg_cust DESC;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print(e)

# For monthly growth
def month_growth():
    with conn:
        try:
            cursor.execute('''WITH monthly_revenue AS(
                                SELECT
                                    EXTRACT(YEAR FROM order_date) AS year,
                                    EXTRACT(MONTH FROM order_date) AS month,
                                    SUM(revenue) AS total_revenue
                                    FROM order_table
                                    GROUP BY year,month
                            ),
                            growth_cal AS(
                                SELECT
                                    year,
                                    month,
                                    total_revenue,
                                    (total_revenue-LAG(total_revenue) OVER(ORDER BY year,month)) AS growth,
                                    (LAG(total_revenue) OVER(ORDER BY year,month)) AS prev_revenue
                                    FROM monthly_revenue
                            )
                            SELECT
                                year,
                                month,
                                prev_revenue,
                                growth,
                                ROUND((growth::NUMERIC/prev_revenue)*100,2) AS "growth(%)"
                                FROM growth_cal;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print(e)

# For quarterly revenue
def quarter_rev():
    with conn:
        try:
            cursor.execute('''SELECT
                                EXTRACT(YEAR FROM order_date) AS year,
                                EXTRACT(QUARTER FROM order_date) AS quarter,
                                SUM(revenue) AS total_rev
                                FROM order_table
                                GROUP BY year,quarter
                                ORDER BY year,quarter;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print(e)

# For running total revenue
def runn_rev():
    with conn:
        try:
            cursor.execute('''WITH curr_rev AS(  
                                SELECT
                                    EXTRACT(YEAR FROM order_date) AS year,
                                    EXTRACT(MONTH FROM order_date) AS month,
                                    SUM(revenue) AS total_rev
                                    FROM order_table
                                    GROUP BY year,month
                            )
                            SELECT
                                year,
                                month,
                                SUM(total_rev) 
                                OVER(ORDER BY year,month) AS runn_rev
                                FROM curr_rev''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print(e)
 
# For moving avg
def mov_avg():
    with conn:
        try:
            cursor.execute('''WITH curr_rev AS(
                                SELECT
                                    EXTRACT(YEAR FROM order_date) AS year,
                                    EXTRACT(MONTH FROM order_date) AS month,
                                    SUM(revenue) AS total_rev
                                    FROM order_table
                                    GROUP BY year,month
                            )
                            SELECT
                                year,
                                month,
                                AVG(total_rev)
                                OVER(ORDER BY year,month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as avg_mov
                                FROM curr_rev;''')
            result=cursor.fetchall()
            return result
        except Exception as e:
            print(e)

