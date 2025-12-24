#1
# ввод целого числа
d = int(input())

if d < 0:
    print(-1 * d)
else:
    print(d)

#2
d1, d2, d3, d4, d5 = map(int, input().split())
print(min(d1, d2, d3, d4, d5))

#3
# ввод целого числа
d1, d2, d3, d4, d5 = map(int, input().split())
print(max(d1, d2, d3, d4, d5))

#4
# ввод данных
a, b = map(int, input().split())
c = (a ** 2 + b ** 2) ** 0.5
print(round(c, 2))

#5
from math import factorial
n, k = map(int, input().split())

C = factorial(n) / (factorial(k) * factorial(n - k))
print(int(C))

#6
from math import ceil
n, m = map(int, input().split())
c = (n + m) / 20
print(ceil(c))

#7
x = int(input())
print(550 // x)