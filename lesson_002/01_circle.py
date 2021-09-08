#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете  S = (PI * radius) ** 2,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

import math
square = (math.pi * radius) ** 2
print(round(square, 4))

# Далее, пусть есть координаты точки
point = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула  так же есть в интернете s_point = (x - center_x) ** 2 + (y - center_y) ** 2 < radius ** 2
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False


origin = (0, 0) #   начало координат (0, 0)
s_point = (point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2
result_1 = s_point < radius ** 2 #  Записываю результат сравнения
print(result_1)


# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.

s_point_2 = (point_2[0] - origin[0]) ** 2 + (point_2[1] - origin[1]) ** 2
result_2 = s_point_2 < radius ** 2
print(result_2)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False

