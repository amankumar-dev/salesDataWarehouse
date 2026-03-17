# A mini data warehouse system that takes raw sales data -> cleans it -> load -> star schema -> KPIs -> Generate business insights

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

# For ETL process
def etl_process_option():
    while((user_input:=input(etl_menu))!='4'):
        if user_input=='1':
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            print('Please choose from the selection !!')

# For Revenue analytics
def revenue_analytics_option():
    while((user_input:=input(revenu_menu))!='5'):
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