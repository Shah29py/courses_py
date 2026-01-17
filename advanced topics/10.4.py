# 1
cmd = input().lower()
match cmd:
    case 'top' | 'bottom' | 'right' | 'left':
        print(f'Команда {cmd}')
    case _:
        print('Неверная команда')

# 2
def get_data(value):
    match value:
        # здесь продолжайте программу
        case str() | int() | float():
            return value
    return None

# 3
def get_data(value):
    match value:
        # здесь продолжайте программу
        case int() as cmd if cmd > 0:
            return value
        case float() as cmd if -100 <= cmd <= 100:
            return value
        case str() as cmd:
            return value

    return None