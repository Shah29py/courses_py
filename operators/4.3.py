# 1
n1 = float(input())
n2 = float(input())
d = n1 if n1 > n2 else n2
print(d)

# 2
number = int(input())
msg = 'кратно 3' if number % 3 == 0 else 'не кратно 3'
print(msg)

# 3
word = input().lower()
msg = 'палиндром' if word == word[::-1] else 'не палиндром'
print(msg)

# 4
number = int(input())
print(bool(number))

# 5
variable = int(input()) + 1
print(variable % 60)

# 6
m = ['0', 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())
a = '#' + m[a] if a == 1 or a == 4 else m[a]
b = '#' + m[b] if b == 1 or b == 4 else m[b]
c = '#' + m[c] if c == 1 or c == 4 else m[c]
print(a, b, c)
