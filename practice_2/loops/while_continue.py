# while loop with continue

n = int(input("Enter a number: "))
i = 0

while i < n:
    i += 1
    if i % 2 == 0:
        continue
    print("Odd number:", i)