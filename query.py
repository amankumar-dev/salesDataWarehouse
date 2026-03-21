from etl import custDf,prodDf

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
    # Standarized the dataframe
    custDf['product_name']=custDf['product_name'].str.title()
    custDf['category']=custDf['category'].str.title()
    
    # Calculating conditions
    total_row=len(custDf)
    dup_row=custDf.duplicated().sum()
    null_val=custDf.isnull().sum().sum()
    
    # Printing details
    print(f'{'='*20} Customer details {'='*20}')
    print('Total rows: ',total_row)
    print('Duplicated rows: ',dup_row)
    print('Null values: ',null_val)
    