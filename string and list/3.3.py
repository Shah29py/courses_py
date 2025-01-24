#1
s = input()
print(s[0].upper() + s[1:].lower())

#2
print(input().count('-'))

#3
print(input().find('ra'))

#4
s = input().replace('---', '-').replace('--', '-')
print(s)

#5
a, b, c = map(str, input().split())
print(a.rjust(3, '0'), b.rjust(3, '0'), c.rjust(3, '0'), sep='\n')

#6
print(len(input().split()))


#7
print(';'.join(input().split()))