from PIL import Image
import numpy as np
from collections import Counter

if __name__ == '__main__':
    img = Image.open('A.bmp')
    pixes = np.array(img)
    k = 0
    l = 0
    for i in pixes:
        for j in i:
            if j == True:
                k += 1
            else:
                l+=1
    print(k, l)