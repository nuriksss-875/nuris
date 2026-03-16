n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0

for i in range(n):
    c = c + a[i] * b[i]
print(c)