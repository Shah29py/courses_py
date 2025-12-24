# 1
gen = (x for x in range(2, 10001))

# 2
# ввод значений a и b (переменные a и b не менять!)
a, b = map(int, input().split())

# здесь продолжайте программу
tp = tuple(x ** 2 for x in range(a, b+1))

# 3
a, b = map(int, input().split())
gen = list(abs(x) for x in range(a, b+1))
print(*(i for i in gen[:5]), sep='\n')

# 4
a = int(input())
gen1 = (abs(x) for x in range(a * (-1), a))
gen2 = (y ** 3 for y in gen1)
print(next(gen2), next(gen2), next(gen2), next(gen2))

# 5
from string import ascii_lowercase as asci


gen = (i + j for i in asci
      for j in asci)
print(*(next(gen) for _ in range(50)))

# 6
cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
gen = (i for _ in range(1000000)
       for i in cities)
print(*(next(gen) for _ in range(20)) )

# 7
a, b = map(int, input().split())
a, b = a*100, b*100
gen = ( (0.5 * pow((x/100),2) - 2) for x in range(a, b+1) )
print( *(round(next(gen), 2) for _ in range(20)) )

