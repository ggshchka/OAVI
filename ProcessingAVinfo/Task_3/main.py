from PIL import Image
import os
import logging
import numpy as np
import contours
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
    img = Image.open('Img1.bmp')
    contours.find_contours(img)[0].save('new_img1.bmp')
    contours.find_contours(img)[1].save('new_img1_x.bmp')
    contours.find_contours(img)[2].save('new_img1_y.bmp')

    #generate(filter.median_filter_mid, 'Median Filter Mid', 5)
    #generate(filter.median_filter_edg, 't3', 5)
    #Image.open("Img6.jpg").save("Img6.bmp")
    #img = Image.open('Img6.bmp')
    #print(np.array(img).shape)
    #filter.median_filter_edg(img, 3).save('NEW.bmp')