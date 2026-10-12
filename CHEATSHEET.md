# 🐍 Python Cheat Sheet

A one-page quick reference for everything covered in the [lessons](README.md#-course-curriculum).

## Basics

```python
print("Hello", name, sep=" ", end="\n")   # output
name = input("Name: ")                     # input is always str
age = int(input("Age: "))                  # cast to int
# comment          """docstring / multi-line"""
```

| Type | Example | Cast |
|---|---|---|
| `int` | `42` | `int("42")` |
| `float` | `3.14` | `float("3.14")` |
| `complex` | `2 + 3j` | `complex(2, 3)` |
| `str` | `"hi"` | `str(42)` |
| `bool` | `True` | `bool(0)` → `False` |
| `NoneType` | `None` | — |

## Operators

```python
+  -  *  /  //  %  **           # arithmetic
==  !=  >  <  >=  <=            # comparison
and  or  not                    # logical
=  +=  -=  *=  /=  //=  **=     # assignment
&  |  ^  ~  <<  >>              # bitwise
is  is not                      # identity
in  not in                      # membership
```

## Strings

```python
s = "Python"
s[0], s[-1], s[1:4], s[::-1]    # 'P' 'n' 'yth' 'nohtyP'
s.upper() s.lower() s.title() s.strip() s.replace("P", "J")
s.split(",")  ",".join(items)  s.find("t")  s.count("o")
s.startswith("Py")  s.isdigit()  len(s)
f"{name} is {age:>3} | {price:.2f} | {big:,} | {ratio:.1%} | {x=}"
```

## Conditions

```python
if x > 0:
    ...
elif x == 0:
    ...
else:
    ...

label = "even" if n % 2 == 0 else "odd"

match command:
    case "start": ...
    case "stop" | "quit": ...
    case _: ...
```

## Loops

```python
for i in range(start, stop, step): ...
for i, item in enumerate(items, start=1): ...
for a, b in zip(list1, list2): ...
while condition: ...
break   continue   pass
for x in data: ... else: ...     # else runs if no break
```

## Collections

| | List | Tuple | Set | Dict |
|---|---|---|---|---|
| Syntax | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"a": 1}` |
| Ordered | ✅ | ✅ | ❌ | ✅ (insertion) |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ | keys ❌ |

```python
# list
lst.append(x) lst.insert(i, x) lst.extend(other) lst.remove(x) lst.pop() lst.sort() lst.reverse() lst.copy()
# tuple
t.count(x) t.index(x)       a, *rest = t
# set
s.add(x) s.discard(x)  a | b  a & b  a - b  a ^ b
# dict
d[k] d.get(k, default) d.keys() d.values() d.items() d.update(other) d.pop(k) d1 | d2
```

## Comprehensions

```python
[x * 2 for x in data if x > 0]          # list
{x % 3 for x in data}                    # set
{k: v for k, v in pairs}                 # dict
(x * x for x in range(10))               # generator
```

## Functions

```python
def greet(name: str, greeting: str = "Hello", *args, **kwargs) -> str:
    """Docstring."""
    return f"{greeting}, {name}!"

square = lambda x: x ** 2
list(map(func, items))  list(filter(func, items))  functools.reduce(func, items)
sorted(items, key=lambda x: x[1], reverse=True)
global x   nonlocal y
```

## Errors

```python
try:
    risky()
except (ValueError, TypeError) as e:
    print(e)
else:
    print("no error")
finally:
    print("always runs")

raise ValueError("message")
class MyError(Exception): pass
```

## Files

```python
with open("file.txt", "w", encoding="utf-8") as f:   # "r" "w" "a" "x" "rb"
    f.write("text\n")
with open("file.txt") as f:
    for line in f: ...

import csv, json
json.dump(obj, f)   json.load(f)   json.dumps(obj)
from pathlib import Path;  Path("dir").mkdir(exist_ok=True)
```

## OOP

```python
class Animal:
    species = "unknown"                    # class attribute
    def __init__(self, name):
        self.name = name                   # instance attribute
        self.__secret = 42                 # private (name-mangled)
    def speak(self): return "..."
    def __str__(self): return self.name
    @property
    def secret(self): return self.__secret
    @classmethod
    def create(cls, name): return cls(name)
    @staticmethod
    def helper(): ...

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self): return "Woof"         # override

from dataclasses import dataclass
from abc import ABC, abstractmethod
```

## Advanced

```python
it = iter(items); next(it)                       # iterators
def gen(): yield 1; yield from other             # generators

def deco(func):                                  # decorators
    @functools.wraps(func)
    def wrapper(*a, **kw): return func(*a, **kw)
    return wrapper

from contextlib import contextmanager            # context managers
import re; re.findall(r"\d+", text)              # regex
if (n := len(data)) > 10: ...                    # walrus
async def main(): await asyncio.sleep(1)         # async
```

## Modules & Environment

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install package     pip freeze > requirements.txt
```

```python
import math, random, datetime, os, sys, collections, itertools
from module import name as alias
if __name__ == "__main__": main()
```
