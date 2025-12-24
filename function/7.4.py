# 1
def get_rect_value(lendth, width, tp=0):
    if tp == 0:
        return lendth * 2 + width * 2
    else:
        return lendth * width

# 2
def check_password(st, chars="$%!?@#"):
    if len(st) > 7 and set(st) & set(chars):
        return True
    else:
        return False

# 3
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


# здесь продолжайте программу
def transliteration(st, sep='-'):
    a = [t[i] if 'а' <= i <= 'я' else i for i in st.lower()]

    return ''.join(a).replace(' ', sep)


string = input()
print(transliteration(string))
print(transliteration(string, sep='+'))

# 4
def f(st, tag='h1'):
    return f'<{tag}>{st}</{tag}>'


check = input()
print(f(check))
print(f(check, tag='div'))


# 5
def f(st, tag='h1', up=True):
    tag = tag.upper() if up else tag.lower()
    return f'<{tag}>{st}</{tag}>'


check = input()
print(f(check, tag='div'))

print(f(check, tag='div', up=False))
