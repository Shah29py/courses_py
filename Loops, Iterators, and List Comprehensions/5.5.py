# 1
array = iter(input().split())
print(next(array))
print(next(array))

# 2
digs = iter(input())
s = ''
while ' ' not in s:
    s += next(digs)
print(s[:-1])

# 3
num = iter(input())
print(next(num), end=' ')
print(next(num), end=' ')
print(next(num), end=' ')
print(next(num))
