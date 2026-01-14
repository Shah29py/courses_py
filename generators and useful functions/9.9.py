# 1
num = map(int, input().split())
ans = all(map(lambda x: x % 2 == 0, num))
print(ans)

# 2
num = map(float, input().split())
ans = any(map(lambda x: x < 0, num))
print(ans)

# 3
def is_string(lst):
    return all(map(lambda x: type(x) == str, lst))

# 4
assessments = map(int, input().split())
status = any(map(lambda x: x < 3, assessments))
print('отчислен' if status else 'учится')

# 5
import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
pole = [i.split() for i in lst_in]


def is_free(lst):
    return any(map(lambda x: '#' in x, lst))