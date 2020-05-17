import pandas as pd
b = pd.read_csv('diamonds.csv', nrows=10)
print(b[['carat','price']])
