# 1
import math

var = float(input())
print(math.ceil(var))

# 2
from math import floor


var = float(input())
print(floor(var))

# 3
from math import factorial as fact


def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p

# 4
from random import seed, randint


seed(1)
print(randint(10, 50))

# 5
from random import seed, random as rnd


seed(10)
print(round(rnd(), 2))

