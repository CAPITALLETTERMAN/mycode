#!/usr/bin/python3

import requests
from mtgsdk import Card
from mtgsdk import Set

CARDSURL = "https://api.magicthegathering.io/v1/cards"

def main():
    """runtime code"""
    magiccards = requests.get(CARDSURL)

    magiccardsjson = magiccards.json()

    print(magiccardsjson)


if __name__ == "__main__":
    main()