# 1
a = tuple(map(int, input().split()))
t = (3.4, -56.7)
t += a
print(t)

# 2
cities = tuple(input().split())
if 'Москва' in cities:
    print(*(cities))
else:
    print(*(cities + ("Москва",)))

# 3
cities = tuple(input().split())
answer = (i for i in cities if i != 'Ульяновск')
print(*answer)

# 4
names = tuple(input().split())
answer = (i.lower() for i in names if 'Ва' in i or 'ва' in i)
print(*answer)

# 5
num = tuple(map(int, input().split()))
ans = ()
for i in num:
    if i not in ans:
        ans += (i,)
print(*ans)

# 6
num = tuple(map(int, input().split()))
ans = [ind for ind, var in enumerate(num) if num.count(var) > 1]
print(*ans)

# 7
t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

N = int(input())

t2 = (i[:N] for i in t if t.index(i) < N)
for i in t2:
    print(*i)

# 8
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
menu = (tuple(i.split()) for i in lst_in)
print(tuple(menu))
