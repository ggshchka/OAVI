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
    Функции median_filter_mid и median_filter_edg
    реализованы для случая окна с фиксированным размером 5х5.
    
    - median_filter_mid - приоритет центра и соседей
    - median_filter_edg - приоритет углов и соседей (в центре 1)
'''
# 5 X 5
@timeit
def median_filter_mid(img):
    core = np.array([[1, 3, 5, 3, 1],
                     [3, 7, 8, 7, 3],
                     [5, 8, 10, 8, 5],
                     [3, 7, 8, 7, 3],
                     [1, 3, 5, 3, 1]])
    border = np.sum(core)/2
    pixes = np.array(img)
    if 255 in pixes:
        pixes = np.divide(pixes, 255)  # нормализация
    size = 5
    pix_val_list = np.zeros((5, 5))
    m = int((size-1)/2)
    for i in range(m, pixes.shape[0] - m):
        for j in range(m, pixes.shape[1] - m):
            for k in range(size):
                for l in range(size):
                    pix_val_list[k, l] = pixes[i - m + k, j - m + l]
            c = np.sum(pix_val_list * core)
            if c > border:
                pixes[i, j] = 1
            else:
                pixes[i, j] = 0
    pixes = pixes * 255 #денормализация
    new_img = Image.fromarray(pixes.astype(np.uint8))
    return new_img

@timeit
def median_filter_edg(img):
    core = np.array([[10, 7, 5, 7, 10],
                     [7, 4, 3, 4, 7],
                     [5, 3, 1, 3, 5],
                     [7, 4, 3, 4, 7],
                     [10, 7, 5, 7, 10]])
    border = np.sum(core)/2
    pixes = np.array(img)
    if 255 in pixes:
        pixes = np.divide(pixes, 255)  # нормализация
    size = 5
    pix_val_list = np.zeros((5, 5))
    m = int((size-1)/2)
    for i in range(m, pixes.shape[0] - m):
        for j in range(m, pixes.shape[1] - m):
            for k in range(size):
                for l in range(size):
                    pix_val_list[k, l] = pixes[i - m + k, j - m + l]
            c = np.sum(pix_val_list * core)
            if c > border:
                pixes[i, j] = 1
            else:
                pixes[i, j] = 0
    pixes = pixes * 255 #денормализация
    new_img = Image.fromarray(pixes.astype(np.uint8))
    return new_img


@timeit
def median_filter_edg_3_3(img):
    core = np.array([[10, 5, 10],
                     [5, 1, 5],
                     [10, 5, 10]])
    border = np.sum(core)/2
    pixes = np.array(img)
    if 255 in pixes:
        pixes = np.divide(pixes, 255)  # нормализация
    size = 3
    pix_val_list = np.zeros((3, 3))
    m = int((size-1)/2)
    for i in range(m, pixes.shape[0] - m):
        for j in range(m, pixes.shape[1] - m):
            for k in range(size):
                for l in range(size):
                    pix_val_list[k, l] = pixes[i - m + k, j - m + l]
            c = np.sum(pix_val_list * core)
            if c > border:
                pixes[i, j] = 1
            else:
                pixes[i, j] = 0
    pixes = pixes * 255 #денормализация
    new_img = Image.fromarray(pixes.astype(np.uint8))
    return new_img



