# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 600)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def fase(coord_x, coord_y, color):
    point_face = sd.get_point(coord_x, coord_y)  # x = 300, y = 300
    radius_face = 50
    sd.circle(center_position=point_face, radius=radius_face, color=color, width=1)
    point_eye_1 = sd.get_point(coord_x - 20, coord_y + 12)
    radius_eye_1 = 5
    sd.circle(center_position=point_eye_1, radius=radius_eye_1, width=1)
    point_eye_2 = sd.get_point(coord_x + 20, coord_y + 12)
    radius_eye_2 = 5
    sd.circle(center_position=point_eye_2, radius=radius_eye_2, width=1)
    start_point_mouth = sd.get_point(coord_x - 20, coord_y - 20)
    end_point_mouth = sd.get_point(coord_x + 20, coord_y - 20)
    sd.line(start_point_mouth, end_point_mouth, width=1)
    radius += step
    sd.circle(center_position=point, radius=radius, width=2)


for _ in range(10):
    point = sd.random_point()
    point = {}
    print(point)
    face(point, color=sd.COLOR_YELLOW)


sd.pause()
