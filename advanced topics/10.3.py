# 1
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
a, b = map(int, input().split())
ans = random.uniform(a, b)
print(round(ans, 2))

# 2
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
a, b = map(int, input().split())
ans = random.randint(a, b)
print(round(ans, 2))

# 3
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
lst = input().split()
print(random.choice(lst))

# 4
import sys
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу
lst = [i.split() for i in lst_in]
lst = list(zip(*lst))
random.shuffle(lst)
lst = list(zip(*lst))
print(*(' '.join(row) for row in lst), sep='\n')

# 5
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]

# здесь продолжайте программу
for i in range(10):
    raw = random.randint(0, N - 1)
    pos = random.randint(0, N - 1)
    if P[raw - 1][pos] == 1 or P[raw][pos - 1] == 1:
        continue
    else:
        P[raw][pos] == 1

print(P)


# 6
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]

# здесь продолжайте программу
k = 0

while k < 10:
    f = random.randint(0, N-1)
    j = random.randint(0, N-1)

    if f % 2 == 0 and j % 2 == 0 and P[f][j] != 1:
        P[f][j] = 1
        k += 1