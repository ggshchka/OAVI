import numpy as np
from PIL import Image
from timeit_decorator import timeit

@timeit
def resample(img, M):
    img_arr = np.array(img)
    new_arr = np.empty([int(img_arr.shape[0]*M), int(img_arr.shape[1]*M), 3])
    for i in range(new_arr.shape[0]):
        for j in range(new_arr.shape[1]):
            new_arr[i][j] = img_arr[int(i * img_arr.shape[0] / new_arr.shape[0])][int(j * img_arr.shape[1] / new_arr.shape[1])]
    new_img = Image.fromarray(new_arr.astype(np.uint8))
    return new_img

@timeit
def resample_two_passes(img, M, N):
    resample(resample(M), 1/N)

