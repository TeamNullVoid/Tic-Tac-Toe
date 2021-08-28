import requests
import random

base_url = "https://tic-tac-toe-py-default-rtdb.firebaseio.com/"
gen = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def generate_key():
    return "".join([random.choice(gen) for _ in range(6)])


print(generate_key())
