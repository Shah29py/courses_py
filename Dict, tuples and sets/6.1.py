# 1
A = [l.split('=') for l in input().split()]
d = {i[0]: int(i[1]) for i in A}
print(*sorted(d.items()))

# 2
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
A = [i.split('=') for i in lst_in]
d = {int(i[0]): i[1] for i in A}
print(*sorted(d.items()))

# 3
lst = [pairs.split('=') for pairs in input().split()]
d = dict(lst)
if ('house' in d) and ('True' in d) and ('5' in d):
    print('ДА')
else:
    print('НЕТ')

# 4
lst = [pairs.split('=') for pairs in input().split()]
d = dict(lst)
if 'False' in d:
    del d['False']

if '3' in d:
    del d['3']
print(*sorted(d.items()))

# 5
lst = input().split()
d = {}
for i in lst:
    d.setdefault(i[:2], []).append(i)
print(*sorted(d.items()))

# 6
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
for i in lst_in:
    d.setdefault(i.split()[1], []).append(i.split()[0])

print(*sorted(d.items()))

# 7
d = {}
while (i := int(input())) != 0:
    if i in d:
        print(f'значение из кэша: {d[i]}')
    else:
        d[i] = round(i ** 0.5, 2)
        print(d[i])

# 8
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {}
for i in lst_in:
    if i in d:
        print(f'Взято из кэша: {d[i]} {i}')
    else:
        d[i] = 'HTML-страница для адреса'
        print(f'{d[i]} {i}')
