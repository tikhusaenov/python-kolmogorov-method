import matplotlib.pyplot as plt
import numpy as np
import statistics as st
from matplotlib import pylab
import scipy.stats as stats


def make_arr():
    data = []
    with open("K_v30b.txt") as file:
        for line in file:
            data = np.append(data, [float(x.replace(',', '.')) for x in line.split()])
    return data


dt = sorted(make_arr())
kol = len(dt)
avg = st.mean(dt)
np.random.seed(2)
x = np.random.normal(loc=avg, scale=0.02, size=kol)
# print(x)

print(stats.ks_2samp(dt, x))
# print(len(dt))

# stats.probplot(dt, dist="norm", plot=pylab)
# pylab.show()

plt.hist(x, 20, density=True)
plt.xlabel('Величина')
plt.ylabel('Кол-во измерений')
plt.title('Нормальное распределение')
plt.grid()
plt.show()
#
plt.hist(dt, 20, density=True)
plt.xlabel('Величина')
plt.ylabel('Кол-во измерений')
plt.title('Гистограмма эмперических данных')
plt.grid()
plt.show()