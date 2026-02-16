# for loop with break

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i == 5:
        print("Breaking the loop at", i)
        break
    print(i)