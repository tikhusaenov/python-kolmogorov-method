import matplotlib.pyplot as plt
import numpy as np
import statistics as st
import scipy.stats as stats


def make_arr():
    data = []
    with open("K_v30c.txt") as file:
        for line in file:
            data = np.append(data, [float(x.replace(',', '.')) for x in line.split()])
    return data


dt = sorted(make_arr())
data_scale = np.std(dt)
kol = len(dt)
avg = np.mean(dt)
x = sorted(np.random.normal(loc=avg, scale=data_scale, size=kol))
print(x)
print(dt)


[statistic, pvalue] = stats.kstest(dt, x, alternative='less')

print(pvalue)


# if(pvalue >= 0.05 and pvalue <= 0.2):
#     print('normal')
# else:
#     print('not normal')



# plt.hist(x, 20, density=True)
# plt.xlabel('Величина')
# plt.ylabel('Кол-во измерений')
# plt.title('Нормальное распределение')
# plt.grid()
# plt.show()
#
#
# plt.hist(dt, 20, density=True)
# plt.xlabel('Величина')
# plt.ylabel('Кол-во измерений')
# plt.title('Гистограмма эмперических данных')
# plt.grid()
# plt.show()