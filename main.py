import numpy as np
from matplotlib import pylab
import scipy.stats as stats


data = []
with open("K_v30a.txt") as file:
    for line in file:
        data = np.append(data, [float(x.replace(',', '.')) for x in line.split()])


print(data)



