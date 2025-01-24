#1
s = input()
print(s[0] + s[-1])

#2
print(input()[:4])

#3
print(input()[-3:])

#4
print(input()[1::2])

#5
print(input()[::2], end=' ')
print(input()[1::2])

#6
s = input()[:5]
s = s[::-1]
print(s)


#7
s1, s2 = map(str, input().split())
print(s2[:len(s1)])

#8
s1, s2 = map(str, input().split())
s1 = s1[:len(s2)]
print(s1[1::2] == s2[1::2])