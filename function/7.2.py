# 1
def get_sq(a):
    return a ** 2


print(get_sq(float(input())))

# 2
def is_triangle(a, b, c):
    return True if (a + b > c) and (a + c > b) and (c + b > a) else False

# 3
def is_large(string):
    return len(string) > 2

# 4
def even(a):
    return x % 2 == 0


while (x := int(input()) ) != 1:
       if even(x):
            print(x)

# 5
def oddness(a):
    return a % 2 == 1


lst_d = list(map(int, input().split()))
lst = [i for i in lst_d if oddness(i)]
print(*lst)

# 6
tp = input().strip()

#здесь продолжайте программу
if tp == "RECT":
    def get_sq(a, b):
        return a * b
else:
    def get_sq(a):
        return a * a


# 7
def check(word):
    return word > 5


cities = input().split()
lst = [x for x in cities if check(len(x))]
print(*lst)


# 8
def MySort(a):
    return a, len(a)


cities = input().split()
d = {MySort(i)[0]: MySort(i)[1] for i in cities}
a = sorted(d, key=d.get)
print(*a)

# 9
def multiplication(a, b):
    return a * b


digs = list(map(int, input().split()))
print(multiplication(min(digs), max(digs)) )
