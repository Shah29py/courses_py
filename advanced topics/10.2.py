# 1
num = int(input())
print(num | 0b1000)

# 2
n = int(input())
mask = 0b10010
print(n & ~mask)

# 3
n = int(input())
mask = 0b1001
print(n ^ mask)

# 4
n = int(input())
print(n << 2)

# 5
n = int(input())
print(n >> 1)

# 6
word = input()
key = 123
ans = list(map(lambda x: chr(ord(x) ^ key), word))
print(''.join(ans))

# 7
n = int(input())
mask = 0b1001000
if n & mask == mask:
    print('ДА')
else:
    print('НЕТ')

# 8
n = int(input())
mask = 0b100010
print('ДА' if n & mask else 'НЕТ')