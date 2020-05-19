import pandas as pd
b=pd.read_csv('diamonds.csv')
print(b.duplicated().sum())
