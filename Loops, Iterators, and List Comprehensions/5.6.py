# 1
N = int(input())
for i in range(N):
    for j in range(N):
        if j == N - 1:
            print(5)
        else:
            print(1, end=' ')

# 3
# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу
for st in lst_in:
    st = st.replace('  ', ' ')
    s = ''
    for j in st:
        if j == " ":
            s += '-'
        else:
            s += j
        if '--' in s:
            s = s.replace("--", "-")
    print(s)

# 4
N = int(input())
for x in range(2, N):
    k = 1
    for j in range(2, x):
        if x % j == 0:
            k = 0
            break
    if k == 1:
        print(x, end=' ')
