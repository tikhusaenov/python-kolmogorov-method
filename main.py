import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
import scipy.stats as stats
from scipy.special import kolmogorov


def make_arr():
    data = []
    with open("K_v30c.txt") as file:
        for line in file:
            data = np.append(data, [float(x.replace(',', '.')) for x in line.split()])
    return data


dt = sorted(make_arr())
print(dt)
print(stats.kstest(dt, 'norm'))

plt.hist(dt, 30, density=True)
plt.xlabel('Величина')
plt.ylabel('Кол-во показаний')
plt.title('Гистограмма измерений')
plt.grid()
plt.show()
#
# stats.probplot(make_arr(), dist="norm", plot=pylab)
# pylab.show()


# def ecdf(dt):
#     """ Compute ECDF """
#     x = np.sort(dt)
#     n = x.size
#     y = np.arange(1, n+1) / n
#     return(x,y)


# x, y = ecdf(dt)
# # mu, sigma = 5, 1
# # rand_normal = np.random.normal(mu, sigma, 100)
# # x, y = ecdf(rand_normal)
# plt.scatter(x=x, y=y)
# plt.show()