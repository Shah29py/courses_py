# 1
words = input().split()
ans = sorted(words, reverse=True, key=len)
print(*ans)

# 2
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)

d = {i.split('=')[0]: int(i.split('=')[1]) for i in lst_in}
new_d = sorted(d, reverse=True, key=lambda x: d.get(x))
print(*new_d)


# 3
notes = input().split()
dct = {'до': 0, 'ре': 1, 'ми': 2, 'фа': 3, 'соль': 4, 'ля': 5, 'си': 6}
notes.sort(key=lambda x: dct.get(x))
print(*notes)

# 4
import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
t_sorted = tuple([
    (name, passed, int(mark) if mark.isdigit() else mark, int(num) if num.isdigit() else num)
    for num, name, mark, passed in [el.split(';') for el in lst_in]
])

# 5
import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
dct = {'рядовой': 0, 'сержант': 1, 'старшина': 2, 'прапорщик': 3, 'лейтенант': 4, 'капитан': 5, 'майор': 6, 'подполковник': 7, 'полковник': 8}
gen = [i.split('=') for i in lst_in]
lst = sorted(gen, key=lambda x: dct.get(x[1]))