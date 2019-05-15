import numpy as np
import pandas as pd



train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

print(train.head())

print(test.head())


raw_input('pause')
print(train)

print('total number of passangers in the training data...', len(train))

print('Number of passangers in the training data who survived...', len(train[train['Survived'] == 1]))


print('% of men who survived', np.mean(train['Survived'][train['Sex'] == 'male']))
print('% of women who survived', np.mean(train['Survived'][train['Sex'] == 'female']))

print('% of passengers who survived in first class', np.mean(train['Survived'][train['Pclass'] == 1]))
print('% of passengers who survived in third class', np.mean(train['Survived'][train['Pclass'] == 3]))


print('% of adults who survived', np.mean(train['Survived'][train['Age'] > 18]))
print('% of children who survived', np.mean(train['Survived'][train['Age'] < 18]))

train['Sex'] = train['Sex'].apply(lambda x: 1 if x == 'male' else 0)



print("test")
print(train['Sex'])
