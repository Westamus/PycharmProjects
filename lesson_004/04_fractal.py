# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 700)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg
# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов (28, 42)
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75 (0.55, 0.95)
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

root_point = sd.get_point(600, 0)


def draw_branches(point, angle, length, delta):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    next_point = v1.end_point
    rand_angle = int(sd.random_number(0, 1))
    if rand_angle == 1:
        delta += sd.random_number(0, 12)
    else:
        delta -= sd.random_number(0, 12)

    rand_length = int(sd.random_number(0, 1))

    coefficient_length = .75
    if rand_length == 1:
        coefficient_length += sd.random_number(1, 20)/100
    else:
        coefficient_length -= sd.random_number(1, 20)/100

    next_angle_right = angle - delta
    next_angle_left = angle + delta
    next_length = length * coefficient_length
    draw_branches(point=next_point, angle=next_angle_right, length=next_length, delta=delta)
    draw_branches(point=next_point, angle=next_angle_left, length=next_length, delta=delta)

draw_branches(point=root_point, angle=90, length=100, delta=30)

sd.pause()
