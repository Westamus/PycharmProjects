# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

x_start = 0
y_start = 0
x_end = 450
y_end = 600
step = 0

for colors in rainbow_colors:
    start_point = sd.get_point(x_start + step, y_start)
    end_point = sd.get_point(x_end + step, y_end)
    sd.line(start_point, end_point, color=colors, width=20)
    step += 20

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


def rainbow(point):
    radius = 600

    for colors in rainbow_colors:
        sd.circle(center_position=point, radius=radius, color=colors, width=20)
        radius -= 20

point = sd.get_point(1000, -100)
rainbow(point=point)

sd.pause()
