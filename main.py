import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
import scipy.stats as stats
from easygui import *
import sys

sys.path.append('..')
import easygui
from tkinter import *

window_size = "750x600"
root = Tk()
root.title("Критерий Колмогорова")
root.geometry(window_size)
labelm = Label(text="Проверка принадлежности выборки \n нормальному распределению методом"
                    "\n критерия Колмогорова", font=("Century Gothic", 11))
labelm.pack()
text = Text(width=80, height=40)


def click_button():
    # Чтение файла, преобразование данных и запись в массив
    f = easygui.fileopenbox()
    text.delete(1.0, END)
    text.insert(1.0, "Вы выбрали файл: \n")
    text.insert(2.0, f)
    text.insert(3.0, "\n \n")

    def make_arr():
        data = []
        with open(f) as file:
            for line in file:
                data = np.append(data, [float(x.replace(',', '.')) for x in line.split()])
        return data

    data_from_array = make_arr()
    text.insert(4.0, "Начальные данные: \n")
    text.insert(5.0, data_from_array)
    text.insert(16.0, "\n \n")

    # Расчет и вывод описательных статистик

    def analyse(value):
        empiric_data = value
        data_kol = len(empiric_data)
        data_avg = np.mean(empiric_data)
        data_std = np.std(empiric_data)
        data_median = np.median(empiric_data)
        criterium = 1.36 / np.sqrt(data_kol)
        print(criterium)
        text.insert(18.0, "Анализ: \n")
        text.insert(19.0, "\n")
        print('Размер выборки:', data_kol)
        text.insert(20.0, "Размер выборки: ")
        text.insert(20.25, data_kol)
        text.insert(21.0, "\n")
        print('Среднее арифметическое значение:', data_avg)
        text.insert(22.0, "Среднее арифметическое значение: ")
        text.insert(22.25, data_avg)
        text.insert(23.0, "\n")
        print('Медиана:', data_median)
        text.insert(24.0, "Медиана: ")
        text.insert(24.25, data_median)
        text.insert(25.0, "\n")
        print('Средне квадратическое отклонение:', data_std)
        text.insert(26.0, "Средне квадратическое отклонение: ")
        text.insert(26.25, data_std)
        text.insert(27.0, "\n \n")
        text.tag_add('title', 1.0, '1.end')
        text.tag_config('title', justify=CENTER, font=("Verdana", 10, 'bold'))
        text.tag_add('title_2', 4.0, '4.end')
        text.tag_config('title_2', justify=CENTER, font=("Verdana", 10, 'bold'))
        return empiric_data, data_kol, data_avg, data_std, criterium

    data_from_analyse = analyse(data_from_array)

    # Генерация нормального распределения и применение метода Колмогорова

    def kolmogorov(data_from_analyse):
        np.random.seed(2)
        data_x = np.random.normal(loc=data_from_analyse[2], scale=data_from_analyse[3], size=data_from_analyse[1])
        print(data_x)
        print(stats.kstest(data_from_analyse[0], data_x))
        text.insert(29.0, "Результаты анализа по критерию Колмогорова: ")
        text.insert(30.0, "\n")
        [statistics, pvalue] = stats.kstest(data_from_analyse[0], data_x)
        if (pvalue > data_from_analyse[4]):
            print('Distribution is normal')
            text.insert(31.0, "Выборка соответствует нормальному распределению")
            text.tag_add('title_3', 31.0, '31.end')
            text.tag_config('title_3', justify=CENTER, font=("Verdana", 10, 'bold'))
            text.insert(32.0, "\n \n")
        else:
            print('Distribution is not normal')
            text.insert(31.0, "Выборка НЕ соответствует нормальному распределению")
            text.insert(32.0, "\n \n \n")

        def show_hist():
            plt.figure(figsize=(7.5, 3))
            plt.rcParams.update({'font.size': 8})
            plt.subplot(121)
            plt.hist(data_x, 20, density=True)
            plt.xlabel('Величина')
            plt.ylabel('Кол-во измерений')
            plt.title('Нормальное распределение')
            plt.grid()
            plt.subplot(122)
            plt.hist(data_from_array, 20, density=True)
            plt.xlabel('Величина')
            plt.ylabel('Кол-во измерений')
            plt.title('Гистограмма эмпирических данных')
            plt.grid()
            plt.show()

        text.insert(32.0, "                             ")
        btn2 = Button(text="Показать гистограммы",  # текст кнопки
                      background="#b3deff",  # фоновый цвет кнопки
                      foreground="#000000",  # цвет текста
                      height="1",
                      padx="20",  # отступ от границ до содержимого по горизонтали
                      pady="5",  # отступ от границ до содержимого по вертикали
                      font=("Century Gothic", 8, "bold"),
                      command=show_hist,
                      justify=CENTER
                      )
        btn2.pack()
        text.window_create(INSERT, window=btn2)

    kolmogorov(data_from_analyse)
    text.pack()


btn = Button(text="Выбрать файл с данными",  # текст кнопки
             background="#a6ddf5",  # фоновый цвет кнопки
             foreground="#000000",  # цвет текста
             height="1",
             padx="20",  # отступ от границ до содержимого по горизонтали
             pady="5",  # отступ от границ до содержимого по вертикали
             font=("Century Gothic", 9, "bold"),
             command=click_button
             )
btn.pack()
label1 = Label(text="Окно для вывода результатов: ", justify=CENTER, font=("Century Gothic", 9))
label1.pack()
text.pack()
root.mainloop()
