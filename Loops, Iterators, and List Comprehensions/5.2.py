# 1
p = [0] * 10
while sum(p) < 5:
    i = int(input())
    if p[i] == 1:
        continue
    p[i] = 1

print(*p)

# 2
s = 1
while (i := int(input())) != 0:
    if i < 0:
        continue
    s *= i

print(s)

# 3
s = input().split()
i = 0
while i < len(s):
    if len(s[i]) < 5:
        print("НЕТ")
        break
    i += 1

else:
    print("ДА")

# 4
s = input().split()
i = 0
while i < len(s):
    if s[i][0].lower() == s[i][-1].lower():
        print("ДА")
        break

    i += 1
else:
    print("НЕТ")

# 5
n = int(input())
array = []
i = 1
while i <= n:
    if n > 99:
        print('слишком большое значение n')
        break
    if i % 3 == 0 and i % 5 == 0:
        array.append(i)

    i += 1
else:
    print(*array)

# 6
n = int(input())
i = 1
while True:
    if i ** 2 > n:
        print(i)
        break
    i += 1

# 7
x = int(input())
s = 10
i = 1
while True:
    if s > x:
        print(i)
        break
    s += (s * 0.1)
    i += 1

# 8
# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines())) # строка стоящая изначально
lst_in = list()
i = 0
array = []
while i < len(lst_in):
    if lst_in[i].count(' ') == 0:
        array.append(lst_in[i])
    i += 1
print(*array)
