import numpy as np
import operator

a=np.array([(1,2,3), (4,5,6)])

print a
print a.ndim
print a.itemsize
print a.size
print a.shape
print a.reshape(3,2)



b=np.array([(1,2,3), (4,5,6), (7,8,9)])

print b
print b[1-1,3-1]
print b[0:, 2-1]
print b[1:3, 2-1]


print np.linspace(1,4,11)


c=np.array([(1,2,3,4), (5,6,7,8), (9,10,11,12), (13, 14, 15, 16)])

print c
print c.min()
print c.max()
print c.sum()
print c.sum(axis=0)
print c.sum(axis=1)
print np.sqrt(c)

d=np.array([(1,2,3,4), (5,6,7,8), (9,10,11,12), (13, 14, 15, 16)])
e=np.array([(1,2,3,4), (5,6,7,8), (9,10,11,12), (13, 14, 15, 16)])

print d
print e
print d+e
print d-e
print d*e
print d/e


x=np.array([(1,2,3),(4,5,6)])
y=np.array([(1,2,3),(4,5,6)])

print np.vstack((x,y))
print np.hstack((x,y))

