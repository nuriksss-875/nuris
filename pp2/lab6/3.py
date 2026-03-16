n = int(input())
a = input().split()

rst = []
for i, j in enumerate(a):
    rst.append(f"{i}:{j}")
print(" ".join(rst)) 
