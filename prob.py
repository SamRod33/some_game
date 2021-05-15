import math
import random as rd


def run(num, denom, a, b, epochs):
    """
    Returns how much money was gained.

    P(a) = num / denom. In the event of P(a), gain $a. Otherwise, gain $b.
    This simulation runs epochs number of times.
    """
    acc = 0
    for i in range(epochs):
        chance = round(rd.uniform(1, denom))
        if chance <= num:
            acc += a
        else:
            acc += b
    return acc


def coin_flip(epochs, fee):
    """
    Returns how much money was gained from the coin flip game.

    You get $2 ^ (n - 1) where n is the total number of heads flipped. 
    For every epoch, you keep flipping until tails is reached. The coin being 
    flipped is a fair coin, i.e. P(heads) = P(tails) = 0.5. During each epoch, 
    you also spend fee dollars.
    """
    acc = 0
    for i in range(epochs):
        n = 0
        chance = round(rd.uniform(1, 2))
        while (chance <= 1):
            n += 1
            chance = round(rd.randint(1, 2))
        if (n > 0):
            acc += 2 ** (n - 1)
        acc -= fee
    return acc


start_run = True
start_coin_flip = False

epochs = 999999
fee = 5
if start_run:
    print(run(1, 2, 100, 0, epochs))
    print(run(1, 2, 50, 50, epochs))
if start_coin_flip and start_run:
    print()
if start_coin_flip:
    print(coin_flip(epochs, fee))
