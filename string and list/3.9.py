#1
lst = [5.4, 6.7, 10.4]

# здесь продолжайте программу
digs = list(map(int, input().split()))
lst += [digs]
print(lst)


#2
lst1 = input().split()
lst2 = input().split()
lst3 = input().split()
print([lst1, lst2, lst3])

#3
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
matrix = [line1] + [line2] + [line3]
print(matrix[0][-1], matrix[1][-1], matrix[2][-1])

#4
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
     ["Я", "Python", "выучил", "с", "каналом"],
     ["Балакирев", "что", "раздавал?"]]
t = sum(t, [])
# здесь продолжайте программу
print(input() in t)