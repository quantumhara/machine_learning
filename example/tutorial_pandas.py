import pandas as pd
import numpy as np
from numpy.random import randn


lst1=['a', 'b', 'c']
lst2=[1, 2, 3]


arr= np.array(lst2)

print pd.Series(lst1)
print pd.Series(lst2, index=lst1)
print pd.Series(arr, index=lst2)


print"*************"

list=["a", "b", "c"]
print list

list_var=list*2
print list_var


ser=pd.Series(list)
print ser

ser_var=ser*2
print ser_var

s1=pd.Series([int(1),int(2)],["math", "english"])
print s1

s2=pd.Series([int(1),int(2)],["math", "japanese"])
print s2

print s1+s2


np.random.seed(101)
df=pd.DataFrame(randn(3,3))
print df

df=pd.DataFrame(randn(3,3),["A", "B", "C"],["D", "E", "F"])
print df

print type(df["E"])
print type(df)

print df.head(2)
print df.tail(1)

print df.isnull().any()

print df.drop('C')
