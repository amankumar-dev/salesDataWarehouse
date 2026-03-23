# A mini data warehouse system that takes raw sales data -> cleans it -> load -> star schema -> KPIs -> Generate business insights
from query import load_cust,load_order,load_prod,load_store,total_revenue,month_revenue,region_revenue
from etl import custDf,factDf,prodDf,storeDf
import calendar

main_menu=f'''
{'='*7} Main Menu {'='*7}
1. Run ETL Process
2. Revenue Analytics
3. Product Analytics
4. Customer Analytics
5. Time Based Analytics
6. Exit

Choose your option: '''

etl_menu=f'''
{'='*7} Run ETL Process {'='*7}
1. Load Dimension Tables
2. Load Fact Table
3. Run Full ETL
4. Back

Choose your option: '''

revenu_menu=f'''
{'='*7} Revenue Analytics {'='*7}
1. Total Revenue
2. Revenue by Month
3. Revenue by Region
4. Revenue by Category
5. Back

Choose your option: '''

prod_menu=f'''
{'='*7} Product Analytics {'='*7}
1. Top 10 Prod by Revenu
2. Least Selling Prod
3. Profit Margin by Prod
4. Category Perform
5. Back

Choose your option: '''

cust_menu=f'''
{'='*7} Customer Analytics {'='*7}
1. Top Customer by Revenue
2. Revenue per Customer
3. Repeat Customer
4. Customer count by Region
5. Back

Choose your option: '''

time_menu=f'''
{'='*7} Time Based Analytics {'='*7}
1. Monthly Growth
2. Quaterly Revenue
3. Running Total Revenue
4. Moving Average
5. Back

Choose your option: '''

# For load dimensions table
def load_dim():
    fun=input('Choose between (Customer/Product/Stores): ')
    if fun=='Customer':
        load_cust(custDf)
    elif fun=='Product':
        load_prod(prodDf)
    elif fun=='Stores':
        load_store(storeDf)
    else:
        print('Please choose from given option !!')

# For load Fact table
def load_fact():
    print('Loading Fact table')
    load_order(factDf)

# For run full etl
def full_etl():
    print('Running full etl')
    print('Removing duplicates...')
    print('Handling Null...')
    print('Handling Date...')
    print('Full ETL complete, Check etl.py for code !!')
    
# For ETL process
def etl_process_option():
    while((user_input:=input(etl_menu))!='4'):
        if user_input=='1':
            load_dim()
        elif user_input=='2':
            load_fact()
        elif user_input=='3':
            full_etl()
        else:
            print('Please choose from the selection !!')

# For total revenue
def total_rev_cal():
    result=total_revenue()
    if(result):
        print(f'{'='*5} Total Revenue {'='*5}')
        print(f'Total Revenue: ₹ {result/10000000:.2f} Cr')
    else:
        print('Something went wrong')

# For month revenue
def month_rev_cal():
    result=month_revenue()
    if result:
        print(f"{'='*5} Monthly Revenue {'='*5}")
        for data in result:
            year=data[0]
            month=data[1]
            revenue=data[2]
            print(f'{calendar.month_abbr[month]} {year} = {revenue}')
    else:
        print('Something went wrong')

# For region revenue
def region_rev_cal():
    data=region_revenue()
    if data:
        print(f"{'='*5} Region Revenue {'='*5}")
        for i in data:
            region=i[0]
            revenue=i[1]
            print(f"{region} = {revenue}")
    else:
        print("Data can't be calculated !!")

def revenue_analytics_option():
    while((user_input:=input(revenu_menu))!='5'):
        if user_input=='1':
            total_rev_cal()
        elif user_input=='2':
            month_rev_cal()
        elif user_input=='3':
            region_rev_cal()
        elif user_input=='4':
            pass
        elif user_input=='5':
            pass
        else:
            print('Please choose from the selection !!')

# For Product analytics
def product_analytics_option():
    while((user_input:=input(prod_menu))!='5'):
        if user_input=='1':
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        elif user_input=='5':
            pass
        else:
            print('Please choose from the selection !!')

# For Customer analytics
def customer_analytics_option():
    while((user_input:=input(cust_menu))!='5'):
        if user_input=='1':
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        elif user_input=='5':
            pass
        else:
            print('Please choose from the selection !!')

# Time Based analytics
def time_based_option():
    while((user_input:=input(time_menu))!='5'):
        if user_input=='1':
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        elif user_input=='5':
            pass
        else:
            print('Please choose from the selection !!')

while((user_input:=input(main_menu))!='6'):
    if user_input=='1':
        etl_process_option()
    elif user_input=='2':
        revenue_analytics_option()
    elif user_input=='3':
        product_analytics_option()
    elif user_input=='4':
        customer_analytics_option()
    elif user_input=='5':
        time_based_option()
    else:
        print('Please choose from the selection !!')