# 1
t = tuple(map(int, input().split()))  # кортеж из целых чисел (в программе не менять)
s = 0  # начальное значение суммы элементов

# здесь продолжайте программу
lst = [s := (s+i) for i in t]
print(*lst)

# 2
# здесь продолжайте программу
ans = 0
while (s := int(input()) ) != 0:
    if s % 2 == 0:
        ans += s
print(ans)

# 3
def f(x):
    return abs(x) ** 0.5 + 3.2 + x


t = tuple(map(float, input().split()))  # кортеж t в программе не менять

# здесь продолжайте программу
lst = [[s := f(entry)**degree for degree in range(1, 4)] for entry in t]

# 4
# здесь пишите программу
ans = 1
while ( s := int(input()) ) > 0:
    if s % 3 == 0:
        ans *= s
print(ans)
