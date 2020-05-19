import pandas as pd

b = pd.read_csv('diamonds.csv')
a=len(b.index)
c=int((len(b.index))*0.75)
d=pd.read_csv('diamonds.csv' ,nrows=c)
print(d)
e=pd.read_csv('diamonds.csv' ,skiprows=c,nrows=(a-c))
print(e)
