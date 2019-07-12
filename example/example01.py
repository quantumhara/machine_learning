import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

dataset=pd.read_csv('car_purch.csv')

print dataset

x=dataset.iloc[:,[2,3]].values
y=dataset.iloc[:,4].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

#print x_train
#print x_test
#raw_input("pause")

sc= StandardScaler()

x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

classifier=LogisticRegression(random_state=0)
classifier.fit(x_train, y_train)

#print classifier.fit(x_train, y_train)
#raw_input("pause")

y_pred=classifier.predict(x_test)

cm=confusion_matrix(y_test, y_pred)

print("")
print("confusion matrix")
print cm
print("")
print("Predicted No", cm[0,0])
print("Predicted Yes", cm[0,1])
print("Actual No", cm[1,0])
print("Actual Yes", cm[1,1])
print("")
print("Accuracy")
print("Match", float(cm[0,0]+cm[1,1])/np.sum(cm))
print("Unmatch", float(cm[0,1]+cm[1,0])/np.sum(cm))
