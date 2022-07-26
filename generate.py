from random import randint

from IteratorAlgorithms import generate


d100 = generate(randint, 1, 100)

for idx, roll in enumerate(d100, 1):
    print(idx, roll)
    if idx >= 10:
        break
