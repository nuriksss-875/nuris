n = int(input())
a = list(map(int, input().split()))

c = []
for i in a:
    c.append(i ** 2)

print(sum(c))    