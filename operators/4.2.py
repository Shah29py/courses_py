# 1
nm = int(input())

if nm == 1:
    print('1. Введение в Python')
elif nm == 2:
    print('2. Строки и списки')
if nm == 3:
    print('3. Условные операторы')
if nm == 4:
    print('4. Циклы')
if nm == 5:
    print('5. Словари, кортежи и множества')
if nm == 6:
    print('6. Выход')

# 2
a, b, c = map(int, input().split())

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)

# 3
weight = float(input())

if 60 >= weight:
    print("1")
elif 64 >= weight:
    print("2")
elif 69 >= weight:
    print("3")
elif 69 < weight:
    print("4")

# 4
day = int(input())

if day == 1:
    print('понедельник')
if day == 2:
    print('вторник')
if day == 3:
    print('среда')
if day == 4:
    print('четверг')
if day == 5:
    print('пятница')
if day == 6:
    print('суббота')
if day == 7:
    print('воскресенье')

# 5
month = int(input()) - 1
array = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(array[month])

# 6
m, n = map(int, input().split())

if n == 1:
    if m == 5 or m == 7 or m == 10 or m == 12:
        print(f'{m - 1:02}.30 {m:02}.02')

    elif m == 2 or m == 4 or m == 6 or m == 8 or m == 9 or m == 11:
        print(f'{m - 1:02}.31 {m:02}.02')

    else:
        print(f'{m - 1:02}.28 {m:02}.02')

elif n == 28:
    if m == 2:
        print(f'{m:02}.27 {m + 1:02}.01')

elif n == 30:
    if m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print(f'{m:02}.29 {m:02}.31')

    elif m == 4 or m == 6 or m == 9 or m == 11:
        print(f'{m:02}.29 {m + 1:02}.01')

elif n == 31:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print(f'{m:02}.30 {m + 1:02}.01')
else:
    print(f'{m:02}.{n - 1} {m:02}.{n + 1}')

# 7
day = int(input())

if day % 7 == 1:
    print('понедельник')
if day % 7 == 2:
    print('вторник')
if day % 7 == 3:
    print('среда')
if day % 7 == 4:
    print('четверг')
if day % 7 == 5:
    print('пятница')
if day % 7 == 6:
    print('суббота')
if day % 7 == 0:
    print('воскресенье')
