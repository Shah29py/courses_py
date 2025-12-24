# 1
n, m = map(int, input().split())
k = n - 1
while k != m:
    k += 1
    print(k ** 2, end=' ')
# 2
num = float(input())
k = 2
while k != 11:
    print(round(num * k, 2), end=' ')
    k += 1
# 3
n = int(input())
k = 0
result = 0
while k != n:
    k += 1
    result += (1 / k)
print(round(result, 3))
# 4
result = 0
while num := int(input()):
    result += num
print(result)

# 5
text = input()
while '--' in text:
    text = text.replace('--', '-')
print(text)

# 6
var = int(input())
result = 1
while var:
    result *= (var % 10)
    var //= 10
print(result)
# 7
n = int(input())
k1, k2 = 1, 1
count = 0
while n != count:
    count += 1
    if count <= 2:
        print(1, end=' ')
    else:
        print(k1 + k2, end=' ')
        k1, k2 = k2, k1 + k2
# 8
n = int(input())
ameba = 1
while n >= 3:
    ameba *= 2
    n -= 3
print(ameba)
# 9
n = int(input())
account = 1000
while n:
    account += account / 20
    n -= 1
print(round(account, 2))
# 10
n, m = map(int, input().split())
while n <= m:
    if n % 2 == 1:
        print(n, end=' ')
    n += 1

# 11
bg, end = 100, 999
while bg <= 999:
    if bg % 47 == 43:
        if bg % 3 == 0:
            print(bg, end=' ')
    bg += 1
