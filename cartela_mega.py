#!/usr/bin/python3

from random import randint

def generateCard():
    amount = input('Quantas cartelas deseja gerar? : ')
    _counter = 0
    while _counter < int(amount):
        card = set()
        while len(card) < 6:
            card.add(randint(1, 60))
        print(sorted(card))
        _counter += 1

generateCard()
