# 1
def parse_json(data):
    match data:
        # здесь прописывайте шаблон
        case {'access': bool() as access, 'data': list([date, *_])}:
            return (access, date)

        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None

json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

# 2
def parse_json(data):
    match data:
        # здесь прописывайте шаблон
        case {'data': [_, {'login': str(login), 'email': str(email)}, *_], 'access': access} if access == True:
            return (login, email)
        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None


json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}