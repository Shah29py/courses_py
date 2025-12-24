# 1
lst = input().split()
lst_abs = [abs(float(i)) for i in lst]
print(lst_abs)

# 2
lst = [int(i) for i in input()]
print(lst)

# 3
N = int(input())
matrix = [print(*[1 if i == j else 0 for j in range(N)]) for i in range(N)]

# 4
cities = [city for city in input().split() if len(city) > 5]
print(*cities)

# 5
n = int(input())
div = [i for i in range(1, n + 1) if n % i == 0]
print(*div)

# 6
N = int(input())
matrix = [print(*[i for j in range(N)]) for i in range(N)]

# 7
numbers = input().split()
ans = [n for i, n in enumerate(numbers) if i % 2 == 0]
print(*ans)

# 8
lst1, lst2 = [int(i) for i in input().split()], [int(i) for i in input().split()]
lst = [lst1[i] + lst2[i] for i in range(len(lst1))]
print(*lst)

# 9
info = input().split()
lst = [[info[i], int(info[i + 1])] for i in range(0, len(info), 2)]
print(lst)
