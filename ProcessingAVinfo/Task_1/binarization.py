from PIL import Image
import numpy as np
import halftoning
from timeit_decorator import timeit


@timeit
def bradley_roth(image):
    img = halftoning.halftone(image)
    img_arr = np.array(img)
    w = img_arr.shape[0]
    h = img_arr.shape[1]
    integral_img_arr = np.empty([w, h])
    new_arr = np.empty([w, h])
    # Интегральное изображение
    for i in range(w):
        sum = 0
        for j in range(h):
            sum += img_arr[i, j]
            if i == 0:
                integral_img_arr[i, j] = sum
            else:
                integral_img_arr[i, j] = integral_img_arr[i-1, j] + sum
    s = w / 8
    t = 15
    for i in range(w):
        for j in range(h):
            x1 = round(i - s / 2)
            x2 = round(i + s / 2)
            y1 = round(j - s / 2)
            y2 = round(j + s / 2)
            if x1 < 0:
                x1 = 0
            if x2 >= w:
                x2 = w - 1
            if y1 < 0:
                y1 = 0
            if y2 >= h:
                y2 = h - 1
            count = (x2 - x1) * (y2 - y1)
            sum = integral_img_arr[x2, y2] - integral_img_arr[x2, y1] - integral_img_arr[x1, y2] + integral_img_arr[x1, y1]
            if (img_arr[i, j] * count) <= (sum * (100 - t) / 100):
                new_arr[i, j] = 0
            else:
                new_arr[i, j] = 255
    new_img = Image.fromarray(new_arr.astype(np.uint8))
    return new_img
