import resampling
import halftoning
import binarization
from PIL import Image
import os
import logging

'''
Функция для генерации изображений
- перебирает все изображения в папке и применяет к ним определенную функцию
- сохраняет новые изображения в другой папке
'''
def generate(operation_func, operation_name, *a):
    logging.basicConfig(filename=r"Logs" "\\" + operation_name + ".log",
                        filemode="w",
                        level=logging.INFO,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

    for filename in os.listdir(r"Pics" "\\" + operation_name):
        if filename.endswith(".bmp"):
            img = Image.open(r"Pics" "\\" + operation_name + "\\" + filename)
            new_img = operation_func(img, *a)
            new_img.save(r"Results" "\\" + operation_name + r"\new_" + filename)
        else:
            print("There are no .bmp files")


if __name__ == '__main__':

    generate(resampling.resample, "Resampling", 2)
    #generate(halftoning.halftone, "Halftoning")
    #generate(binarization.bradley_roth, "Binarization")


    img = Image.open('Img7.bmp')
    new_img = halftoning.halftone(img)
    new_img.save(r'Img7.bmp')
