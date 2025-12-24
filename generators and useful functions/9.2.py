# 1
# ввод значения N (эту переменную не менять)
N = int(input())

# здесь продолжайте программу
def get_sum(total):
    for i in range(1, total+1):
        yield sum(range(1, i+1))

# 2
N = int(input())


def balak_seq(max_len):
    n1, n2, n3 = 1, 1, 1
    for i in range(max_len):
        if i < 3:
            yield 1
        else:
            ans = n1 + n2 + n3
            yield ans
            n1 = n2
            n2 = n3
            n3 = ans


func = balak_seq(N)
for _ in range(N):
    print(next(func), end=' ')

# 3
import random
from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
# установка зерна датчика случайных чисел (не менять)
random.seed(1)


# здесь продолжайте программу
def gen_password(length):
    # indx = random.randint(0, len(chars)-1)
    while True:
        password = ''
        for i in range(length):
            indx = random.randint(0, len(chars) - 1)
            password += chars[indx]
        yield password


N = int(input())
func = gen_password(N)
for _ in range(5):
    print(next(func))

# 4
from string import ascii_lowercase, ascii_uppercase
import random

chars = ascii_lowercase + ascii_uppercase
random.seed(1)


def get_random_email(max_size):
    while True:
        password = ''
        for i in range(max_size):
            indx = random.randint(0, len(chars) - 1)
            password += chars[indx]
        yield password + '@mail.ru'


N = int(input())
for _ in range(5):
    print(next(get_random_email(N)))

# 5
def simple_num():
    for num in range(2, 100):
        flag = 0
        counter = 0
        for i in range(2, num):
            if num % i == 0:
                flag = 1
                break
        else:
            if counter <= 20:
                yield num
                counter += 1

func = simple_num()
for _ in range(20):
  print(next(func), end=' ')

