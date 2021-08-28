from firebase import firebase
import random

base_url = "https://tic-tac-toe-py-default-rtdb.firebaseio.com"
gen = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

firebase = firebase.FirebaseApplication(base_url, None)


def generate_key():
    return "".join([random.choice(gen) for _ in range(6)])


def create_data(key, player):
    return {
        "turn": player,
        "joined": False,
        "moves": "000000000",
        "created_by": player,
        "winner": 0,
        "code": key
    }


def create_game(player):
    key = generate_key()
    data = create_data(key, player)
    result = firebase.put('/games', key, data)
    print(result)
    return key


def connect(key):
    result = firebase.patch('/games/' + key, {"joined": True})
    print(result)


def disconnect(key):
    result = firebase.patch('/games/' + key, {"joined": False})
    print(result)
