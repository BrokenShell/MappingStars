""" Generators """
from itertools import count


def counter(n: int):
    c = count(n)
    while True:
        yield next(c)


def counter2(n: int):
    yield from count(n)


my_counter = counter(1)

for i in my_counter:
    print(i)
    if i > 4:
        break

print("stop")

for i in my_counter:
    print(i)
    if i > 9:
        break
