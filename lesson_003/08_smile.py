# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 600)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(coord_x, coord_y, color):
    point_face = sd.get_point(coord_x, coord_y)  # Координаты лица
    radius_face = 50  # Размер лица
    sd.circle(center_position=point_face, radius=radius_face, color=color, width=1)  # Фигура лица
    point_eye_1 = sd.get_point(coord_x - 20, coord_y + 12)  # Координаты правого глаза
    radius_eye_1 = 5  # Размер левого глаза
    sd.circle(center_position=point_eye_1, radius=radius_eye_1, width=1)  # Фигура левого глаза
    point_eye_2 = sd.get_point(coord_x + 20, coord_y + 12)  # Координаты левого глаза
    radius_eye_2 = 5  # Размер правого глаза
    sd.circle(center_position=point_eye_2, radius=radius_eye_2, width=1)  # Фигура правого глаза
    start_point_mouth = sd.get_point(coord_x - 20, coord_y - 20)  # Левая точка рта
    end_point_mouth = sd.get_point(coord_x + 20, coord_y - 20)  # Правая точка рта
    sd.line(start_point_mouth, end_point_mouth, width=1)  # Фигура рта


for _ in range(10):  # Вывести 10 раз на экран рандомно смайлик
    coord = sd.random_point()  # Рандомные координаты x = XXX, y = YYY
    coord_x = coord.x  # Извлекаем координату x
    coord_y = coord.y  # Извлекаем координату y
    smile(coord_x, coord_y, color=sd.COLOR_YELLOW)  # Рисуем смайлик

sd.pause()
