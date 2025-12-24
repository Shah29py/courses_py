# 1
# считывание числа N
N = int(input())

#здесь продолжайте программу
def get_rec_N(x):
    if 1 != x:
        get_rec_N(x - 1)
    print(x)



get_rec_N(N) # вызов рекурсивной функции

# 2
lst = list(map(int, input().split()))

def get_rec_sum(array, ans=0, key=0):
    if len(array):
        ans += array.pop()
        if len(array) == 0 and key == 0:
            key = 1
            print(ans)
        get_rec_sum(array, ans, key)

get_rec_sum(lst)

# 3
# ввод числа N
N = int(input())


# здесь задается функция fib_rec (переменную N не менять!)
def fib_rec(N, f=[1, 1]):
    if len(f) < N:
        f.append(f[-1] + f[-2])
        return fib_rec(N, f)
    return f

# 4
# ввод числа n
n = int(input())


# здесь задается функция fact_rec  (переменную n не менять!)
def fact_rec(n):
    if n <= 1:
        return 1

    return n * fact_rec(n - 1)

# 5
d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


# здесь продолжайте программу
def get_line_list(d, a=[]):
    for item in d:
        if type(item) == list:
            get_line_list(item, a)
        else:
            a.append(item)
    return a

# 6
N = int(input())

def get_path(N):
    if N == 1 or N == 2:
        return N

    return get_path(N-1) + get_path(N-2)

print(get_path(N))

# 7
numbers = list(map(int, input().split()))


def merge_two_list(lst1, lst2):
    final_list = []
    i = j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            final_list.append(lst1[i])
            i += 1
        else:
            final_list.append(lst2[j])
            j += 1

    if i < len(lst1):
        final_list += lst1[i:]

    if j < len(lst2):
        final_list += lst2[j:]

    return final_list


def sort_divide(lst):
    if len(lst) == 1:
        return lst

    n = len(lst) // 2
    left = sort_divide(lst[:n])
    right = sort_divide(lst[n:])
    return merge_two_list(left, right)


print(*sort_divide(numbers))

