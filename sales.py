import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'C:\Users\tanto\Documents\sere\liquorsales.csv')
df = df.reset_index()

df_new = pd.DataFrame()

zipcpde_grp = df.groupby(['zip_code'])
sales_per_zipcode = zipcpde_grp['bottles_sold'].sum()
zip_codes = sales_per_zipcode.index
sales = list(sales_per_zipcode)


for zipcode, sale in zip(zip_codes, sales):
    plt.scatter(zipcode, sale)

plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.show()



