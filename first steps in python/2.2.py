#1
a = 7
b = -4
c = 3
print(a, b, c)

#2
a = 7
b = -4
c = 3
print(a, b, c, sep='\n')

#3
s1 = "Hello"
s2 = "Balakirev"
print(s1, end=' ')
print(s2)

#4
s1, s2 = map(str.strip, input().split())
print(f'Word 1: {s1}', f'Word 2: {s2}', sep=' | ')

#5
a, b = map(int, input().split())
print(a ** b)

#6
a, b = map(float, input().split())
print(a + b)

#7
X, Y = map(int, input().split())
black = X * 2
red = Y * 4
print(X + Y + black + red)

#8
print((float(input()) + float(input()) ) * 2)

#9
from math import pi

print(round(pi, 3))

#10
print(f"Вы ввели число {input()}")