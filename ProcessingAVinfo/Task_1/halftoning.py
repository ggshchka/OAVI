from timeit_decorator import timeit
import numpy as np
from PIL import Image

@timeit
def halftone(img):
    img_arr = np.array(img)
    #coef = [1/3, 1/3, 1/3]
    coef = [0.3, 0.59, 0.11]
    new_arr = np.dot(img_arr[..., :3], coef)               #Скалярное произведение ([m,n,3] * [3, 1] = [m,n])
    new_img = Image.fromarray(new_arr.astype(np.uint8))
    return new_img