#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Андрей', 'Лена', 'Эдуард', 'Егор', 'Кирилл']


# список списков приблизителного роста членов вашей семьи
my_family_height = [['Андрей', 185], ['Лена', 165], ['Эдуард', 166], ['Егор', 125], ['Кирилл', 105]]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца -', my_family_height[0][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
summa_my_family_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1]
print('Общий рост моей семьи -', summa_my_family_height, 'см')