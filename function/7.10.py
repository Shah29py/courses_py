# 1
def counter_add():
    def add_5(x):
        x += 5
        return x
    return add_5


cnt = counter_add()
k = int(input())
print(cnt(k))

# 2
def counter_add(n):
    def add_n(x):
        x += n
        return x

    return add_n


cnt = counter_add(2)
k = int(input())
print(cnt(k))

# 3
def lock_in_tag():
    def transformation(string):
        return f'<h1>{string}</h1>'

    return transformation


cnt = lock_in_tag()
word = input()
print(cnt(word))

# 4
def tag_in_lock(tag):
    def add_string(string):
        return f'<{tag}>{string}</{tag}>'

    return add_string


cnt = tag_in_lock(input())
print(cnt(input()))

# 5
def type_collection(tp):
    def collection(array):
        if tp == 'list':
            return list(array)
        else:
            return tuple(array)

    return collection


cnt = type_collection(input())
numbers = map(int, input().split())
print(cnt(numbers))
