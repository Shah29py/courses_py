# 1
word = input().lower()
k = 0
for i in range(len(word) - 1):
    if word[i:i + 2] == 'ра':
        print(i, end=' ')
        k = 1
else:
    if k == 0:
        print(-1)

# 2
num = input()

if num[0] == '+' and num[1] == '7' and num[2] == '(' and \
        num[6] == ')' and num[10] == '-' and num[13] == '-':

    for i in range(len(num)):
        if num[i] in '0123456789' or (i in [0, 1, 2, 6, 10, 13]):
            continue
        else:
            print('НЕТ')
            break
    else:
        print('ДА')
else:
    print('НЕТ')

# 3
example = input().replace(' ', '')
if '+' in example:
    example = ' + '.join(example.split('+'))
if '-' in example:
    example = ' - '.join(example.split('-'))

ex = example.split(' ')
sum = int(ex[0])
for i in range(len(ex) - 1):
    if ex[i] == '+':
        sum += int(ex[i + 1])
    elif ex[i] == '-':
        sum -= int(ex[i + 1])

print(sum)

# 4
digs = input().split()

for i, n in enumerate(digs):
    digs[i] = int(n) ** 2
print(*digs)

# 5
array = input().split()
for i in array:
    print(i, i, end=' ')

# 6
array = list(map(float, input().split()))
mi = array[0]
for i in array:
    if mi > i:
        mi = i

print(mi)

# 7
array = list(map(float, input().split()))
for i, n in enumerate(array):
    if n < 0:
        array[i] = -1.0
print(*array)
