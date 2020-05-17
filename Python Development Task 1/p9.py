import pandas as pd
b = pd.read_csv('diamonds.csv')
print(b.groupby('cut').price.agg(['count', 'min', 'max']))
