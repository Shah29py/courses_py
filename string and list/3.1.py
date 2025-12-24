#1
print(f'{input()} {input()}')

#2
a, b = map(str, input().split())
print((a + ' ') * 2 + (b + ' ') * 3)

#3
a, b = map(str, input().split())
print('Переменная a = ' + a + ', переменная b = ' + b)

#4
a = input()
print('Строка: ' + a + '. Длина:', len(a))

#5
a, b = map(str, input().split())
print(a in b, a == b, a > b, a < b)

#6
a, b = map(str, input().split())
print(f'Коды: {a} = {ord(a)}, {b} = {ord(b)}')