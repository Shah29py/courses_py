# 1
cities = filter(lambda x: len(x) > 5, input().split())
print(next(cities), next(cities), next(cities))

# 2
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
pairs = map(lambda x: tuple(x.split('=')), lst_in)
selection = filter(lambda a: int(a[1]) > 500, pairs)
print(*(i[0] for i in selection))

# 3
two_digit = filter(lambda x: 10 > (abs(int(x)) // 10) > 0, input().split())
print(*two_digit)

# 4
a = set(map(int, input().split()))
b = set(map(int, input().split()))
answer = filter(lambda x: x % 2 == 0, a & b)
print(*sorted(answer))

# 5
symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890.@"
data = input().split()
true_email = filter(lambda mail: all(x in symbols for x in mail) and mail.index('.') > mail.index('@') , data)
print(*true_email)