# DS Workshop: Mapping the Stars

### Workshop Outline
0. Introduction & Motivation
1. Iterators
2. Generators
3. Generate
4. Mapping the Stars


---
## 0. Introduction & Motivation `main.py`
Lists are great, but have you ever tried to make a list of infinite items? Iterators can do it.

All Generators are Iterators, but not all Iterators are Generators. Generators are custom Iterators. Technically, they are function-like objects that produce custom Iterators. Today we'll take a look at some basic Iterators and Generators, then we'll see some special Generators.


---
## 1. Iterators `iterators.py`
Iterators are like recipes for producing sequences of values. Another way to say that is, Iterators are like virtual lists. Iterators consume their values as they're produced, similar to `List.pop()`. Only one value from an iterator is ever in RAM at any given time. This makes Iterators highly efficient. Iterators remember where they stopped and can continue. Once an Iterator is consumed it can no longer produce values.

### Check For Understanding
1. True or False. Once an iterator has been exhausted it automatically restarts from the beginning.
2. True or False. If an iterator is stopped prematurely it can be restarted from where it left off.
3. True or False. An iterator is like a virtual list, or a recipe for generating values.

### CFU Answers
1. False. There are iterators that can do this, but this is not the default behavior.
2. True.
3. True. It's considered virtual because the values do not occupy RAM like a list of values would.


---
## 2. Generators `generators.py`
We can define them much like functions. Generators use `yield` rather than `return` to produce values. In Python, `yield` is like `return` but `yield` allows stopping and restarting from where it stopped. Typically, `yield` (by itself) appears inside a loop, sometimes an infinite loop like `while True`. Conversely, `yield from` requires that we already have an iterator to yield from, and no loop is needed.

### Check For Understanding
1. True or False. Generators look like functions that yield instead of return.
2. True or False. A Generator is one type Iterator.
3. True or False. All Iterators are Generators.

### CFU Answers
1. True.
2. True.
3. False. All Generators are Iterators, not the other way around.

---
## 3. IteratorAlgorithms.generate `generate.py`
Generate, from the `IteratorAlgorithms` Library by Robert Sharp. This generator takes a function and parameters and produces an infinite iterator of function calls with its parameters.

```python
from typing import Callable, Iterator

def generate(func: Callable, *args, **kwargs) -> Iterator:
    while True:
        yield func(*args, **kwargs)
```

### Check For Understanding
1. True or False. Generate is part of the standard library.
2. True or False. Infinite iterators are dangerous for low memory hardware.

### CFU Answers
1. False. Generate is from the IteratorAlgorithm library by Robert Sharp.
2. False. On the contrary, they make it possible to do the impossible on cheap hardware. You still need to be mindful of infinite loops.


---
## 4. Mapping the Stars `mapping_stars.py`
Map is great, but have you ever tried sending it a function that requires more than one input? Starmap can do it. `itertools.starmap`

Our mission is to map the stars, unfortunately a flat map isn't good enough, we need a starmap! As you may remember from a previous workshop, map takes a function and an iterable as its inputs. The function should take one and only one input, this translates to each value from the iterable, one at a time. What if the function we want to use requires more than one input? 

We have a few options and Starmap is one of them. Here's the signature of starmap in sudo code...

```
starmap(F: Callable[[*H], Value], G: Iterable[H: Iterable...]) -> Iterator[Value]
```

The Callable F, must take a number of inputs equal to the length of H. The length of G controls how many calls to F(*H) we get when the resulting Iterator is consumed.

Zip is often employed to package the inputs together. Starmap automatically unpacks the tuples that zip creates and feeds them to our function. The result is an iterator that calls that function repeatedly, presumably with different inputs each time.

### Check For Understanding
1. True or False. Starmap, like Generate uses the same inputs for each call to the callable.
2. True or False. Both Generate and Starmap follow the iterator protocol.
3. True or False. Zip, map, filter and starmap can all be used together like puzzle pieces because they all follow the iterator protocol.

### CFU Answers
1. False. This is where Generate and Starmap differ significantly.
2. True.
3. True.
