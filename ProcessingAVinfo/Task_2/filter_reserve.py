import numpy as np
from PIL import Image
from timeit_decorator import timeit
import itertools as it

'''
        Медианный фильтр  -  один из видов цифровых фильтров, 
     широко используемый в цифровой обработке сигналов и 
     изображений для уменьшения уровня.
        Значения отсчётов внутри окна фильтра сортируются в 
     порядке возрастания (убывания); и значение, находящееся 
     в середине упорядоченного списка, поступает на выход 
     фильтра. Окно перемещается вдоль фильтруемого сигнала 
     и вычисления повторяются.
'''

'''
    Функции median_filter_mid_3_3 и median_filter_edg_3_3
    реализованы для случая окна с фиксированным размером 3х3.
    Немножко захардкожено.
'''

''' 
приоритет центра и соседей     
         3x3
        0 1 0
        1 1 1
        0 1 0
'''


@timeit
def median_filter_mid_3_3(img):
    pixes = np.array(img)
    pix_val_list = [0] * 5
    for i in range(1, pixes.shape[0] - 1):
        for j in range(1, pixes.shape[1] - 1):
            pix_val_list[0] = pixes[i - 1, j]
            pix_val_list[1] = pixes[i, j - 1]
            pix_val_list[2] = pixes[i, j]
            pix_val_list[3] = pixes[i, j + 1]
            pix_val_list[4] = pixes[i + 1, j]
            pixes[i, j] = np.median(pix_val_list)
    new_img = Image.fromarray(pixes.astype(np.uint8))
    return new_img


''' 
приоритет углов и соседей
         3x3
        1 0 1
        0 1 0
        1 0 1
'''


@timeit
def median_filter_edg_3_3(img):
    pixes = np.array(img)
    pix_val_list = [0] * 5
    for i in range(1, pixes.shape[0] - 1):
        for j in range(1, pixes.shape[1] - 1):
            pix_val_list[0] = pixes[i - 1, j - 1]
            pix_val_list[1] = pixes[i - 1, j + 1]
            pix_val_list[2] = pixes[i, j]
            pix_val_list[3] = pixes[i + 1, j - 1]
            pix_val_list[4] = pixes[i + 1, j + 1]
            pixes[i, j] = np.median(pix_val_list)
    new_img = Image.fromarray(pixes.astype(np.uint8))
    return new_img


'''
    Следующие функции - median_filter_edg и median_filter_mid
    обобщены. Размер окна можно задать при вызове функций (по умолчанию 3х3).

    - median_filter_mid - приоритет центра и соседей
    - median_filter_edg - приоритет углов и соседей (в центре 1)
'''

'''                 Окно
         i-3 i-2 i-1  i  i+1 i+2 i+3

  j-3     10   x   x   -   x   x   10
  j-2     x   x   -   -   -   x   9
  j-1     x   -   4   -   4   -   8
    j     -   -   -   1  -   -   -
  j+1     x   -   4   3   4   -   8
  j+2     x   x   -   5   6   7   9
  j+3     10   x   x   7   8   9   10

  На входе бинарное изображение.
  Наложить на рисунок. На выходе бинарное изображение.
   > 50  = white
   < 50 = black
   ]

'''

@timeit
def median_filter_edg(img, size=3):
    pixes = np.array(img)
    pix_val_list = [0] * int((size * size + 1) / 2)
    m = int((size - 1) / 2)
    for i in range(m, pixes.shape[0] - m):
        for j in range(m, pixes.shape[1] - m):
            t = 0
            for k in range(i - m, i):
                for l in it.chain(range(j - m, j - m + (i - k)), range(j + m - (i - k) + 1, j + m + 1)):
                    pix_val_list[t] = pixes[k, l]
                    t += 1
            for k in range(i + 1, i + m + 1):
                for l in it.chain(range(j - m, j - m + (k - i)), range(j + m - (k - i) + 1, j + m + 1)):
                    pix_val_list[t] = pixes[k, l]
                    t += 1
            pix_val_list[int((size * size + 1) / 2) - 1] = pixes[i, j]
            pixes[i, j] = np.median(pix_val_list)
    new_img = Image.fromarray(pixes.astype(np.uint8))
    return new_img


'''                  Окно
         i-3 i-2 i-1  i  i+1 i+2 i+3

  j-3     -   -   -   x   -   -   -
  j-2     -   -   x   x   x   -   -
  j-1     -   x   x   x   x   x   -
    j     x   x   x   x   x   x   x
  j+1     -   x   x   x   x   x   -
  j+2     -   -   x   x   x   -   -
  j+3     -   -   -   x   -   -   -
'''

@timeit
def median_filter_mid(img, size = 3):
    pixes = np.array(img)
    pix_val_list = [0] * int((size * size + 1) / 2)
    m = int((size - 1) / 2)
    for i in range(m, pixes.shape[0] - m):
        for j in range(m, pixes.shape[1] - m):
            t = 0
            for k in range(i - m, i):
                for l in range(j - m + (i - k), j + m - (i - k) + 1):
                    pix_val_list[t] = pixes[k, l]
                    t += 1
            for k in range(i, i + m + 1):
                for l in range(j - m + (k - i), j + m - (k - i) + 1):
                    pix_val_list[t] = pixes[k, l]
                    t += 1
            pixes[i, j] = np.median(pix_val_list)
    new_img = Image.fromarray(pixes.astype(np.uint8))
    return new_img