# 1
def get_even(*args):
    ans = [i for i in args if i % 2 == 0]
    return ans

# 2
def get_biggest_city(*args):
    return max(args, key=len)

# 3
def get_data_fig(*args, **kwargs):
    perimeter = sum(args)
    result = [perimeter]
    for param in ['tp', 'color', 'closed', 'width']:
        if param in kwargs:
            result.append(kwargs[param])
    return tuple(result)


# 4
import sys


# здесь объявляйте функцию
def is_isolate(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):  # сравниваем только уникальные пары
            if abs(lst[i][0] - lst[j][0]) < 2 and abs(lst[i][1] - lst[j][1]) < 2:
                return False
    return True


def verify(lst2D):
    lst = []
    for i, row in enumerate(lst2D):
        for j, val in enumerate(row):
            if val == 1:
                lst.append((i, j))
    return is_isolate(lst)



lines = sys.stdin.readlines()  # чтение строк из входного потока (переменную lines не менять)
lst2D = [list(map(int, x.strip().split())) for x in lines]  # формирование матрицы чисел

# 5
def str_min(var1, var2):
    if var1 < var2:
        return var1
    else:
        return var2


def str_min3(var1, var2, var3):
    return str_min(str_min(var1, var2), var3)


def str_min4(var1, var2, var3, var4):
    return str_min(str_min3(var1, var2, var3), var4)

