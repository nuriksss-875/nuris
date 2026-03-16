n = input()
a = "aeiouAEIOU"
c = False
for i in range(len(a)):
    if a[i] in n:
        c = True
if c:
    print("Yes")
else:
    print("No")