# 1
var = input().split()
k = int(var.pop(0))
action = {k+i: var[i] for i in range(len(var))}
print(action[4])

# 2
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
action = {x for x in lst_in}
print(len(action))

# 3
words = input().lower().split()
action = {x for x in words if len(x) >= 3}
print(len(action))

# 4
lst = input().lower().split()
action = {x: lst.count(x) for x in lst}
print(action.get('и', 0))

# 5
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {x.split(':')[0]: {y.split(': ')[1] for y in lst_in if x.split(':')[0] == y.split(':')[0]}
          for x in lst_in}
