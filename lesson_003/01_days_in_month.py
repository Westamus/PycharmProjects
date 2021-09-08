# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
user_input = int(user_input)
month = int(user_input)
print('Вы ввели', month)
month_days_31 = [1, 3, 5, 7, 8, 10, 12]
month_days_30 = [4, 6, 9, 11]

for days in month_days_31:
    if days == user_input:
        print('Дней в этом месяце -', 31)
        break

for days in month_days_30:
    if days == user_input:
        print('Дней в этом месяце -', 30)
        break

if user_input == 2:
    print('Дней в этом месяце -', 28)


