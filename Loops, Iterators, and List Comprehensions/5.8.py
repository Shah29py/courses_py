# 1
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
M =[x
    for row in lst_in[::-1]
    for x in row[::-1]
    ]
print(*M)

# 2
lst_in = list(map(int, input().split()))
N = int(len(lst_in) ** 0.5)
lst = [[lst_in[i] for i in range(j, j + N)]
       for j in range(0, N * N, N)
       ]

print(lst)

# 3
t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]

lst = [[w for w in row.split() if len(w) > 3]
       for row in t
      ]
print(lst)

# 4
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

A = [[lst_in[j][i] for j in range(len(lst_in))]
     for i in range(len(lst_in[0]))
    ]
for row in A:
    print(*row)