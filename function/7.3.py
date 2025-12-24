# 1
def get_nod(a, b):
    while b:
        a, b = b, a % b
    return a
