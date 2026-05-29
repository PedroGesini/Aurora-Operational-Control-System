import json

def carregar_dados():
    with open("data/data.json", "r", encoding="utf-8") as arquivo:
        banc = json.load(arquivo)

    return banc