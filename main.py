import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
import scipy.stats as stats
from scipy.stats import norm


def make_arr():
    data = []
    with open("K_v30c.txt") as file:
        for line in file:
            data = np.append(data, [float(x.replace(',', '.')) for x in line.split()])
    return data




data = make_arr()
def ecdf():
    x = np.sort(data)
    n = x.size
    y = np.arange(1, n+1) / n
    return x, y


print(ecdf())



# print(stats.kstest(data_array, 'norm',))
# stats.probplot(data_array, dist="norm", plot=pylab)
# pylab.show()


