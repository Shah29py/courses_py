# 1
def decorator_st(start):
    def decorator_func(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + start

        return wrapper

    return decorator_func


@decorator_st(start=5)
def get_integer(numbers):
    numbers = map(int, numbers.split())
    return sum(numbers)


var = get_integer(input())
print(var)

# 2
def decorator_tag(tag='h1'):
    def decorator_func(func):
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'

        return wrapper

    return decorator_func


@decorator_tag(tag='div')
def str_lower(string):
    return string.lower()


s = input()
print(str_lower(s))

# 3
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


# здесь продолжайте программу
def decorator_char(chars='!?'):
    def decorator_func(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            res = ''.join(['-' if i in chars else i
                           for i in res])
            while '--' in res:
                res = res.replace('--', '-')
            return res

        return wrapper

    return decorator_func


@decorator_char("?!:;,. ")
def get_lower_str(string):
    string = string.lower()
    string = [t.get(i, i) for i in string]
    return string


s = get_lower_str(input())
print(s)

# 4
from functools import wraps

# здесь продолжайте программу
def sum_list(func):
    @wraps(func)
    def wrapper(*args):
        result = sum(func(*args))
        return result
    return wrapper

@sum_list
def get_list(numbers):
    '''Функция для формирования списка целых значений'''
    return list(map(int, numbers.split()))

