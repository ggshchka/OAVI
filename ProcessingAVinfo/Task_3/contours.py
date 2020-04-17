from PIL import Image
import numpy as np
from timeit_decorator import timeit
from Task_2.filter import median_filter_edg
from Task_1.halftoning import halftone


def find_contours(img):
    ht_img = halftone(img)
    smoo_img = median_filter_edg(ht_img, 3)
    pixes = np.array(smoo_img)
    width = pixes.shape[0]
    height = pixes.shape[1]
    pixes_x = np.empty((width, height))
    pixes_y = np.empty((width, height))
    G = np.empty((width-1, height-1))
    grad_G_x = np.empty((width - 1, height - 1))
    grad_G_y = np.empty((width - 1, height - 1))
    for i in range(1, width-1):
        for j in range(1, height-1):
            G_x = (3 * pixes[i - 1, j - 1] + 10 * pixes[i - 1, j] + 3 * pixes[i - 1, j + 1]) - (
                        3 * pixes[i + 1, j - 1] + 10 * pixes[i + 1, j] + 3 * pixes[i + 1, j + 1])

            G_y = (3 * pixes[i - 1, j - 1] + 10 * pixes[i, j - 1] + 3 * pixes[i + 1, j - 1]) - (
                        3 * pixes[i - 1, j + 1] + 10 * pixes[i, j + 1] + 3 * pixes[i + 1, j + 1])
            grad_G_x[i, j] = abs(G_x)
            grad_G_y[i, j] = abs(G_y)
            G[i, j] = abs(G_x) + abs(G_y)
    max_el_in_G = np.amax(G)
    max_el_in_G_x = np.amax(grad_G_x)
    max_el_in_G_y = np.amax(grad_G_y)
    for i in range(1, width-1):
        for j in range(1, height-1):
            pixes[i, j] = int(G[i, j] * 255/max_el_in_G)
            pixes_x[i, j] = int(grad_G_x[i, j] * 255/max_el_in_G_x)
            pixes_x[i, j] = int(grad_G_y[i, j] * 255 / max_el_in_G_y)

    new_img = Image.fromarray(pixes.astype(np.uint8))
    new_img_x = Image.fromarray(pixes_x.astype(np.uint8))
    new_img_y = Image.fromarray(pixes_y.astype(np.uint8))
    return new_img, new_img_x, new_img_y