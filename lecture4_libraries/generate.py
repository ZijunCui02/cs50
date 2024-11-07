# import random
from random import choice
from random import randint
from random import shuffle

# coin = random.choice(["1","2","3","4","5"])
coin = choice(["1","2","3","4","5"])
print (coin)

number = randint(1,10)
print(number)

cards = ["Jack", "Queen", "King"]

# random.shuffle(x)
shuffle(cards)

for card in cards:
    print(card)
print()

for card in range(len(cards)):
    print(cards[card])
