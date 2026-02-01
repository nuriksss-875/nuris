# for loop with continue

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    print("Not divisible by 3:", i)