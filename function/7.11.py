# 1
def func_show(func):
    def wrapper(*args):
        print(f'Площадь прямоугольника: {func(*args)}')

    return wrapper


def get_sq(width, height):
    return width * height

# 2
menu = input()  # чтение пунктов меню (переменную menu не менять)


def show_menu(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        for num, i in enumerate(args[0].split()):
            print(f'{num + 1}. {i}')

    return wrapper


@show_menu
def get_menu(s):
    s = s.split()
    return s

# 3
def sort_list(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        lst = ''.join(args)
        lst = list(map(int, lst.split()))
        return sorted(lst)

    return wrapper


@sort_list
def get_list(s):
    s = s.split()
    return s


res = get_list(input())
print(*res)

# 4
def get_dict(func):
    def wrapper(a, b):
        var1, var2 = func(a, b)[0], func(a, b)[1]
        d = dict(zip(var1, var2))
        return d

    return wrapper


@get_dict
def get_list(a, b):
    array1 = a.split()
    array2 = b.split()
    return array1, array2


d = get_list(input(), input())
print(*sorted(d.items()))

# 5
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


# здесь продолжайте программу
def cleaning(func):
    def wrapper(lst):
        res = ''.join(func(lst))
        res = res.replace(' ', '-')
        while '--' in res:
            res = res.replace('--', '-')
        return res

    return wrapper


@cleaning
def transliteration(string):
    lst = [t[i] if 'а' <= i <= 'я' else i for i in string.lower()]
    return lst


result = transliteration(input())
print(result)
