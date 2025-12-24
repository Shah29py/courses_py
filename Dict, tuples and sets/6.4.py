# 1
numbers = set(map(float, input().split()))
print(*sorted(numbers))

# 2
words = set(input().lower().split())
print(len(words))

# 3
txt = set(input().split())
ans = (i for word in txt
       for i in word if i in '0123456789'
      )
ans = list(ans)
print(*sorted(set(ans)) if ans else ['НЕТ'])

# 4
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
print(len(set(lst_in)))

# 5
import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
ans = set(words.split(':')[0] for words in lst_in)
print(len(ans))

# 6
s = set()
while (var := input()) != 'q':
    s.add(var)
print(len(s))