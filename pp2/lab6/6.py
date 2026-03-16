n = int(input())
a = list(map(int, input().split()))

c = True
for i in range(n):
    if a[i] < 0:
        c = False
if c:
    print("Yes")
else:
    print("No")