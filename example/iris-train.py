from sklearn import svm, metrics
import random, re

csv = []

with open("iris.csv", "r", encoding="utf-8") as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(",")
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

del csv[0]

random.shuffle(csv)

total_len = len(csv)
train_len= int(total_len * 2/3)
train_data = []
train_data = []train_data = []
