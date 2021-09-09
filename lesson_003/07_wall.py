# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

step = 50
reset_var = 100
left_x = 0
left_y = 0
rigth_x = 100
rigth_y = 50
for i in range(6):  # колличество прогонов по 2 ряда вверх
    for y in range(0, 51, 50):  # копирует 1-й ряд кирпичей
        for x in range(0, 701, 100):  # копирует 1 ряд из 6 кирпичей
            left_bottom = sd.get_point(left_x + x, left_y + y)
            right_top = sd.get_point(rigth_x + x, rigth_y + y)
            sd.rectangle(left_bottom, right_top, color=sd.COLOR_DARK_RED, width=1)  # рисует 1 ряд кирпичей
        left_x += step
        rigth_x += step
    left_x = 0
    left_y = reset_var
    rigth_x = 100
    rigth_y = reset_var + 50
    reset_var += 100

sd.pause()
