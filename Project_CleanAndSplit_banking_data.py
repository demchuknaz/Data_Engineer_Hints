import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
bank_marketingDF = pd.read_csv('bank_marketing.csv')

print(bank_marketingDF.head(15))
print(bank_marketingDF.dtypes)

# Client's type of job	Change "." to "_"

# Check if there are any duplicates and print a sum of them

duplicates = bank_marketingDF.duplicated(subset = ["client_id"], keep= False)
print(duplicates)
print(f"Total rows involved in duplicates: {duplicates.sum()}")

# Fix multiple columns at once
cols_to_fix = ['job', 'education']

for col in cols_to_fix:
    bank_marketingDF[col] = bank_marketingDF[col].str.replace('.', '_', regex=False)

bank_marketingDF['education'] = bank_marketingDF['education'].replace('unknown', np.NaN)
    
print(bank_marketingDF.head(50))