# 1
*lst, x, y, z = map(int, input().split())
print(*lst)

# 2
a = input().split()
lst_c = *a,
print(lst_c)

# 3
a = map(int, input().split())
lst = list(range(*a))
print(*lst, lst[-1] + 1)

# 4
float_num = map(float, input().split())
cities = input().split()
lst = [*float_num, *cities]
print(*lst)

# 5
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)
dict_in = {i.split("=")[0]:i.split("=")[1] for i in lst_in}
menu = {**dict_in, **menu}
