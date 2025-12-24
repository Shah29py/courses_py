# 1
num = map(float, input().split())
print(next(num), next(num), next(num))

# 2
num_mod = list(map(lambda x: abs(int(x)), input().split()))
print(*num_mod)

# 3
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
# переменную lst_in не менять!
lst2D = list(map(lambda line: [int(i) for i in line.split()], lst_in))

# 4
# ввод строки (переменную s не менять)
s = input()
s_lst = s.split()

# здесь продолжайте программу
tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))

# 5
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '-'}

# здесь продолжайте программу
words = input().lower()
lst = list(map(lambda x: t[x], words))
print(''.join(lst))

# 6
cities = map(lambda x: x if len(x) > 5 else '-', input().split())
print(*cities)

