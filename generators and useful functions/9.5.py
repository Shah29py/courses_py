# 1
numbers1 = map(int, input().split())
numbers2 = map(int, input().split())
mult = lambda x: x[0] * x[1]

answer = zip(numbers1, numbers2)
print(mult(next(answer)), mult(next(answer)), mult(next(answer)))

# 2
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
gen = [i.split() for i in lst_in]
selection = zip(*gen)
answer = zip(*selection)
print(*(' '.join(row) for row in answer), sep='\n')

# 3
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
gen = [i.split() for i in lst_in]
matrix = zip(*gen)
print(*(' '.join(line) for line in matrix), sep='\n')

# 4
line = input().split()
ans = zip(*[iter(line)] * 3)
print(*(' '.join(i) for i in ans), sep='\n')

# 5
# считывание строки в переменную s (эту переменную в программе не менять)
s = input()

# здесь продолжайте программу
lst = list(zip(s, range(10)))