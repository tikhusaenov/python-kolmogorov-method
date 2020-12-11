import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
import scipy.stats as stats


def make_arr():
    data = []
    with open("K_v30a.txt") as file:
        for line in file:
            data = np.append(data, [float(x.replace(',', '.')) for x in line.split()])
    return data



print(stats.kstest(make_arr(),'norm'))
plt.hist(make_arr())
plt.show()
