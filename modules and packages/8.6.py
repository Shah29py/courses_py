# 1
try:
    f = open("abc.txt")
    r = f.read(1)
    f.close()
except FileNotFoundError:
    print("File Not Found")

# на тему исключений даётся лишь одна задача, рекомендую отработать тему в сторонних источниках
