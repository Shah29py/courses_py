# 1
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

print(*sorted(setA & setB))

# 2
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

print(*sorted(setA - setB))

# 3
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

print(*sorted(setA ^ setB))

# 4
setA = set(input().split())
setB = set(input().split())

print('ДА' if setA >= setB else 'НЕТ')

# 5
setA = set(map(int, input().split()))

print('НЕ ДОПУЩЕН' if setA & {2} else 'ДОПУЩЕН')

# 6
setA = set(input().split())
setB = set(input().split())

print('ДА' if setA <= setB else 'НЕТ')

# 7
num = int(input())
primes = [2, 3, 5, 7]
factors = set()
check = [factors.add(i) for i in primes if num % i == 0]
print('ДА'if {2, 3, 5} <= factors else 'НЕТ')
