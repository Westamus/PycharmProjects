import requests
# задаем список сайтов
url = ['https://gta-max.com/',
       'https://www.rbc.ru/',
       'https://www.promelec.ru/',
       'https://www.kommersant.ru/',
       'http://techosmotr-ekb.ru/']

# Перебираем в цикле сайты
for i in range(5):
    print(url[i])
    a = 0 # Переменная для перебора
    while a <= 9:
        response = requests.get(url[i])  # Запрос к сайту
        print(a + 1,') ',response.status_code)
        a += 1




# for urls in url:
#     i = 0
#     print(urls)
#     while i <= 99:
#         print(i + 1,') ',response.status_code)
#         i += 1


# for url_1 in range(5):
#     i = 0
#     print(url_1)
#     while i <= 99999:
#         print(i + 1,') ',response.status_code)
#         i += 1

# for i in range(150):
#     response = requests.get('https://jo-jo.ru')
#     print(response.status_code)