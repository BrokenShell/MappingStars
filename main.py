from itertools import islice, cycle
from string import ascii_lowercase


def count(n):
    i = n
    while True:
        yield i
        i += 1


counter = count(1)
for number in islice(counter, 5):
    print(number)


def alpha():
    yield from cycle(ascii_lowercase)


a = alpha()
for letter in islice(a, 26):
    print(letter)
