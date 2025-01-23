#1
a, b, c = map(int, input().split())
print([a, b, c])


#2
print('Москва' in input().split())

#3
print(input().split()[-1])


#4
marks = list(map(int, input().split()))
print(round(sum(marks)/len(marks), 1))


#5
book = [input(), input(), input(), float(input())]
del book[2]
book[1] = 'Пушкин'
book[2] *= 2
print(book)

#6
lst = list(map(int, input().split()))
print(max(lst), min(lst), sum(lst))

#7
lst = list(map(int, input().split()))
print(*sorted(lst, reverse=1))

#8
cities = ["Москва", "Тверь", "Вологда"]
lst = cities + list(map(str, input().split()))
print(*lst)

#9
cities = ["Москва", "Тверь", "Вологда"]
lst = list(input().split()) + cities
print(*lst)