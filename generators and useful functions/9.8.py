# 1
def get_add(a, b):
    if type(a) in (int, float) and type(b) in (int, float):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b

# 2
def get_sum(it):
    ans = sum(filter(lambda x: type(x) is int, it))
    return ans

# 3
def get_even_sum(it):
    ans = filter(lambda x: type(x) in (int, float) and x % 2 == 0, it)
    return sum(ans)

# 4
def get_list_dig(lst):
    ans = filter(lambda x: type(x) in (int, float), lst)
    return list(ans)