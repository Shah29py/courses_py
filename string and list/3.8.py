#1
a = list(map(int, input().split()))
a.append(a[0] != a[-1])
print(*a)

#2
cities = ["Москва", "Казань", "Ярославль"]
cities.insert(1, 'Ульяновск')
print(*cities)

#3
a = list(input())
a = a[2:]
a.insert(0, '8')
a.remove("-")
a.remove("-")
print("".join(a))

#4
a = list(map(str, input().split()))
lst = f'{a[2]} {a[0][0]}.{a[1][0]}.'
print(lst)

#5
array = map(int, input().split())
array = sorted(array)[:3]
print(*array)

#6
lst = list(map(int, input().split()))
lst[-1] = bool(lst[-1] % 2)
print(*lst)


#7
lst = list(map(int, input().split()))
a = lst.count(2)
print(a)

#8
lst = list(map(str, input().split()))
lst.sort()
del lst[0]
print(*lst)