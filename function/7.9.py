# 1
WIDTH = int(input())


def func1():
    global WIDTH
    WIDTH += 1
    return WIDTH


print(func1())

# 2
def func1():
    msg = input()


    def func2():
        nonlocal msg
        msg = input()
        print(msg)


    func2()
    print(msg)


func1()

# 3
def create_global(x):
    global TOTAL
    TOTAL = x
    