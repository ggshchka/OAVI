from PIL import Image
import os
import logging
import numpy as np
import filter
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
    #Image.open("Img.png").save("Img3.bmp")
    generate(filter.median_filter_edg_3_3, 'Median Filter Edg')
    #generate(filter.median_filter_edg_3_3, 'Median Filter Edg')


    #Image.open("Img6.jpg").save("Img6.bmp")
    #img = Image.open('Img3.bmp')
    #img = img.convert('1').save('Img3.bmp')
    #filter.median_filter_edg(img).save('NEW.bmp')

