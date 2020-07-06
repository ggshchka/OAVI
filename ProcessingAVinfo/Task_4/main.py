from PIL import Image
import os
import signs
'''
Функция для генерации изображений
- перебирает все изображения в папке и применяет к ним определенную функцию
- сохраняет новые изображения в другой папке
'''
def generate(operation_func, *a):
    for filename in os.listdir(r"Symbols"):
        if filename.endswith(".bmp"):
            img = Image.open(r"Symbols" "\\" + filename)
            operation_func(img, filename)
        else:
            print("There are no .bmp files")


if __name__ == '__main__':
    generate(signs.pretty_output)