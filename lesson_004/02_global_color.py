# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def figure(start_point, side_count, angle, length, color):
    vector = start_point
    angle_step = 360 / side_count
    step = angle_step
    for side in range(side_count):
        if side == 0:
            vector = sd.get_vector(start_point=vector, angle=angle, length=length + 3)
        elif side == side_count - 1:
            sd.line(vector.end_point, start_point, color=color)
            break
        else:
            vector = sd.get_vector(start_point=vector.end_point, angle=angle + step, length=length)
            step += angle_step
        vector.draw(color=color)


side_input = int(input('Какую фигуру вам нарисовать (3,4,5,6,..):'))
color_dict = {1: 'COLOR_RED', 2: 'COLOR_ORANGE', 3: 'COLOR_YELLOW',
              4: 'COLOR_GREEN', 5: 'COLOR_CYAN', 6: 'COLOR_BLUE', 7: 'COLOR_PURPLE'}
# for color_list range(6):
#     color_tuple = dict(color_dict)
#     print()
length_input = 100  # int(input('Какая длина стороны:'))
x = 300  # input('Укажите координату x:')
y = 300  # input('Укажите координату y:')
angle_input = 0  # int(input('Под каким углом повернуть фигуру:'))
point = sd.get_point(x, y)
color = sd.COLOR_RED
figure(start_point=point, side_count=side_input, angle=angle_input, length=length_input, color=color)

sd.pause()
