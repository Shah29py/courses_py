# 1
def send():
    print("It's my first function")


send()

# 2
def send(name):
    print(f"Уважаемый, {name}! Вы верно выполнили это задание!")


send(input())

# 3
def send_weight(weight):
    print(f"Предмет имеет вес: {weight} кг.")


send_weight(float(input()))

# 4
def MySort(lst):
    Min = min(lst)
    Max = max(lst)
    Sum = sum(lst)
    print(f"Min = {Min}, max = {Max}, sum = {Sum}")


MySort([int(i) for i in input().split()])

# 5
def perimeter(width, height):
    print(f"Периметр прямоугольника, равен {width * 2 + height * 2}")


perimeter(*map(int, input().split()))

# 6
def mail_check(email):
    if False not in (
    i if ('a' <= i <= 'z') or ('A' <= i <= 'Z') or ('0' <= i <= '9') or ("@" == i) or ('.' == i) or (i == '_') and (
            "@" in email and '.' in email) else False for i in email):
        print("ДА")
    else:
        print("НЕТ")


mail_check(input())
