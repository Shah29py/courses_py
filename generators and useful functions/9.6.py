# 1
# ввод строки в переменную s (переменную в программе не менять)
s = input()

# здесь продолжайте писать программу
lst = list(map(int, s.split()))
tp_lst = tuple(lst)
lst.sort()
tp_lst = tuple(sorted(tp_lst))

# 2
def get_sort(d):
    keys = sorted(d.items(), reverse=True)
    return list(dict(keys).values())

# 3
num = set(map(int, input().split()))
res = sorted(num, reverse=True)
print(*res[:4])

# 4
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
res = map(sum, zip(a, b))
print(*res)

# 5