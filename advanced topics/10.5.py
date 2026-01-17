# 1
t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case str() as author, name:
        print('Yes')
    case author, name, price:
        print('Yes')
    case author, name, price, *_:
        print('Yes')
    case _:
        print('No')

# 2
t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]

match book:
    case [_, author, name] if len(author) >= 6 and len(name) >= 10:
            print('Yes')
    case [_, author, name, float() as price] if price > 0:
        print('Yes')
    case [_, author, name, _, int() as year] if year >= 2020:
        print('Yes')
    case [_, author, name, price, year] if price > 0 and year >= 2020:
        print('Yes')
    case _:
        print('No')