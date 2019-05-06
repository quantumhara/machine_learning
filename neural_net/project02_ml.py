from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

xs=np.array([1,2,3,4,5,6], dtype=np.float64)
ys=np.array([5,4,6,5,6,7], dtype=np.float64)

def best_fit_slope_intercept(xs,ys):
    m=((np.mean(xs)*np.mean(ys))-(np.mean(xs*ys)))/((np.mean(xs)*np.mean(xs))-(np.mean(xs*xs)))
    b=np.mean(ys)-m*np.mean(xs)
    return m,b

def squared_error(ys_orig, ys_line):
    return sum((ys_orig-ys_line)**2)

def coefficient_of_determination(ys_orig,ys_line):
    ys_mean_line=[mean(ys_orig) for y in ys_orig]
    square_error_regr=squared_error(ys_orig, ys_line)
    square_error_y_mean=squared_error(ys_orig, ys_mean_line)
    return 1-(square_error_regr/square_error_y_mean)

m,b=best_fit_slope_intercept(xs,ys)

print(m,b)

regression_line=[(m*x)+b for x in xs]
#for x in xs:
#    regression_lin.append()

predict_x=8
predict_y=m*predict_x+b

style.use('fivethirtyeight')

r_squared=coefficient_of_determination(ys,regression_line)

print(r_squared)

plt.scatter(xs,ys)
#plt.plot(xs,ys)
plt.scatter(predict_x,predict_y, color='g')
plt.plot(xs,regression_line)
plt.show()
