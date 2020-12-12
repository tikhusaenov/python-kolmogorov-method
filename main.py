import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
import scipy.stats as stats


# Чтение файла, преобразование данных и запись в массив

def make_arr():
    data = []
    with open("K_v30a.txt") as file:
        for line in file:
            data = np.append(data, [float(x.replace(',', '.')) for x in line.split()])
    return data


data_from_array = make_arr()

# Расчет и вывод описательных статистик


def analyse(value):
    empiric_data = value
    data_kol = len(empiric_data)
    data_avg = np.mean(empiric_data)
    data_std = np.std(empiric_data)
    data_median = np.median(empiric_data)
    criterium = 1.36/np.sqrt(data_kol)
    print(criterium)
    print('Размер выборки:', data_kol)
    print('Среднее арифметическое значение:', data_avg)
    print('Медиана:', data_median)
    print('Средне квадратическое отклонение:', data_std)
    return empiric_data, data_kol, data_avg, data_std, criterium


# Генерация нормального распределения и применение метода Колмогорова


def kolmogorov(data_from_analyse):
    np.random.seed(2)
    data_x = np.random.normal(loc=data_from_analyse[2], scale=data_from_analyse[3], size=data_from_analyse[1])
    print(data_x)
    print(stats.kstest(data_from_analyse[0], data_x))
    [statistics, pvalue] = stats.kstest(data_from_analyse[0], data_x)
    if(pvalue > data_from_analyse[4]):
        print('Distribution is normal')
    else:
        print('Distribution is not normal')


if __name__ == "__main__":
    data_from_array = make_arr()
    data_from_analyse = analyse(data_from_array)
    kolmogorov(data_from_analyse)










# plt.hist(data_x, 20, density=True)
# plt.xlabel('Величина')
# plt.ylabel('Кол-во измерений')
# plt.title('Нормальное распределение')
# plt.grid()
# plt.show()
# #
# # plt.hist(dt, 20, density=True)
# # plt.xlabel('Величина')
# # plt.ylabel('Кол-во измерений')
# # plt.title('Гистограмма эмперических данных')
# # plt.grid()
# # plt.show()