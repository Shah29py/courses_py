# 1
words = input().split()
ans = sorted(words, reverse=True, key=len)
print(*ans)

# 2
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)

d = {i.split('=')[0]: int(i.split('=')[1]) for i in lst_in}
new_d = sorted(d, reverse=True, key=lambda x: d.get(x))
print(*new_d)


# 3


# 4


# 5