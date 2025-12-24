# 1
get_sq = lambda x: x ** 2

# 2
get_div = lambda x, y: None if (x == 0 or y == 0) else x / y

# 3
x = (lambda x: abs(x))(float(input()))
print(x)

# 4
s = (lambda x: 'ra' in x)(input())
print(s)

# 5
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

# здесь продолжайте программу
digs = list(map(int, input().split()))

print(*filter_lst(digs))
print(*filter_lst(digs, lambda x: x < 0))
print(*filter_lst(digs, lambda x: x >= 0))
print(*filter_lst(digs, lambda x: 3 <= x <= 5))

