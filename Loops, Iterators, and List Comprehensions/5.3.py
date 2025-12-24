# 1
for i in range(11):
    print(i, end=' ')

# 2
for i in range(-10, 1):
    print(i, end=' ')

# 3
for i in range(-10, -1, 2):
    print(i, end=" ")

# 4
for i in range(1, 20, 3):
    print(i, end=" ")

# 5
array = map(int, input().split())
answer = 0
for i in array:
    if i % 2:
        answer += i
print(answer)

# 6
array = input().split()
for i in array:
    print(len(i), end=' ')

# 7
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# 8
n = int(input())
for i in range(2, round(n ** 0.5) + 1):
    if n % i == 0:
        print('НЕТ')
        break
else:
    print("ДА")

# 9
cities = input().split()
for i in range(len(cities) - 1):
    if cities[i][-1] not in 'ь ъ ы':
        if cities[i][-1].lower() != cities[i + 1][0].lower():
            print('НЕТ')
            break
    else:
        if cities[i][-2].lower() != cities[i + 1][0].lower():
            print('НЕТ')
            break
else:
    print('ДА')

# 10
n = int(input())
k = 0
for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
        k += i
print(k)
