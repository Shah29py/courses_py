#1
print(f'Уважаемый {input()} {input()}! Поздравляем Вас с {input()}-летием!')

#2
print(f"Габариты: {input().replace(' ', ' x ')}")

#3
a, b = map(int, input().split())
print(f'{min(a, b)} {max(a, b)}')

#4
print(f"г. {input()}, ул. {input()}, д. {input()}, кв. {input()}")


#5
a, b = float(input()), int(input())
print(f"Вы можете получить {int(b) // int(a)}$ за {b} рублей по курсу {a}")