#1
print(int(float(input())) % 3 == 0)

#2
print(float(input()) % 1 > 0.5)

#3
a, b = map(int, input().split())
print(a % b == 0)

#4
a, b, c = map(int, input().split())
print(a + b > c and a + c > b and b + c > a)

#5
a = float(input())
print(0 <= a <= 2 or 10 <= a <= 20)