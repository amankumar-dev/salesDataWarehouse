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