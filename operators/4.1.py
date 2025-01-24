# 1
v1, v2 = map(float, input().split())
if v1 > v2:
    print(v1)
else:
    print(v2)

# 2
word = input()
if word.lower() == word[::-1].lower():
    print("ДА")
else:
    print("НЕТ")

# 3
v1, v2 = map(int, input().split())
if v1 % v2 == 0:
    print(v1 // v2)
else:
    print(f'{v1} на {v2} нацело не делится')

# 4
a, b, c = map(int, input().split())
if (a ** 2 + b ** 2) == c ** 2:
    print("ДА")
else:
    print("НЕТ")

# 5
a, b, c = map(int, input().split())
if (a ** 2 + b ** 2) == c ** 2:
    print("ДА")
else:
    print("НЕТ")

# 6
word = input().lower()
if 't' in word and 'h' in word and 'o' in word:
    print('ДА')
else:
    print('НЕТ')

# 7
cities = input().split()
if 'Москва' in cities:
    cities.remove('Москва')
print(*cities)

# 8
a, b, c, d = map(int, input().split())
if (a > c + 1 and b > d + 1) or (b > c + 1 and a > d + 1):
    print('ДА')
else:
    print('НЕТ')

# 9
value = int(input())
if sum(map(int, str(value // 1000))) == sum(map(int, str(value % 1000))):
    print('ДА')
else:
    print('НЕТ')

# 10
color = float(input()) % 5
if color < 3:
    print('green')
else:
    print('red')
