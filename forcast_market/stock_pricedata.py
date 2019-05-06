import pandas as pd

from pandas_datareader import data, wb

import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

start = datetime.datetime(2018,1,21)
end = datetime.datetime(2018,1,31)

df = data.DataReader('F', 'google', start, end)

print(df.head())
