import pandas as pd
import quandl, math, datetime
import time
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


df =quandl.get("EOD/V", authtoken="coj_xSs_vsFtRXmmDo89")

df = df [['Adj_Open', 'Adj_High', 'Adj_Low', 'Adj_Close', 'Adj_Volume',]]
df['high&low_PCT'] = (df['Adj_High']-df['Adj_Close'])/df['Adj_Close'] * 100.0
df['percentage_change'] = (df['Adj_Close']-df['Adj_Open'])/df['Adj_Open'] * 100.0

df = df[['Adj_Close', 'high&low_PCT', 'percentage_change', 'Adj_Volume']]

print "original data"
print(df.head())
print "******************************"

forecast_col = 'Adj_Close'
df.fillna(-99999, inplace=True) # inplace:

forecast_out = int(math.ceil(0.01*len(df)))
print 'forecast_out=', forecast_out, 'days'


df['label'] = df[forecast_col].shift(-forecast_out) # shift negative
#df.dropna(inplace=True) # dropna

print(df.head())

x=np.array(df.drop(['label'], 1))
x=preprocessing.scale(x)
#x=x[:-forecast_out+1]
x=x[:-forecast_out]
x_lately=x[-forecast_out:]

df.dropna(inplace=True) # dropna
#y=np.array(df['label'])
#df.dropna(inplace=True)
y=np.array(df['label'])

x_train, x_test, y_train, y_test=cross_validation.train_test_split(x, y, test_size=0.2)

clf=LinearRegression(n_jobs=4)
#clf=svm.SVR()
#clf=svm.SVR(kernel='poly')
clf.fit(x_train, y_train)


# pickle
with open('linearregression.pickle','wb') as f:
    pickle.dump(clf, f)
pickle_in=open('linearregression.pickle','rb')
clf=pickle.load(pickle_in)



accuracy=clf.score(x_test, y_test)

#print 'accuracy=', accuracy

forecast_set=clf.predict(x_lately)

print 'forecast_set'
print forecast_set
print ''
print 'accuracy and forecast_out'
print accuracy, forecast_out


df['forecast']=np.nan

last_date=df.iloc[-1].name
#last_unix=last_date.timestamp()
last_unix=time.mktime(last_date.timetuple())

one_day=86400
next_unix=last_unix+one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date]=[np.nan for _ in range(len(df.columns)-1)]+[i]

print(df.tail())

df['Adj_Close'].plot()
df['forecast'].plot()

plt.legend(loc=4)
plt.xlabel('date')
plt.ylabel('price')
plt.show()
