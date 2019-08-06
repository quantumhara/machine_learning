import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree



iris = load_iris()

print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])

for i in range(len(iris.target)):
    print("Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i]))


test_indx = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_indx)
train_data = np.delete(iris.data, test_indx, axis=0)

# test data
test_target = iris.target[test_indx]
test_data = iris.data[test_indx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print("classes= ", test_target)
print("test_data= ", test_data)

print(clf.predict(test_data))



# visualization

import graphviz

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")

dot_data = tree.export_graphviz(clf, out_file=None,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     special_characters=True)
graph = graphviz.Source(dot_data)
graph

"""
from sklearn.externals.six import StringIO
import pydot

dot_data = StringIO()

tree.export_graphviz(clf,
                     out_file = dot_data,
                     feature_names = iris.feature_names,
                     class_names = iris.target_names,
                     filled = True, rounded = True,
                     impurity = False)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")
"""
