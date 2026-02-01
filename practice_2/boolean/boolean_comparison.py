x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

is_greater = x > y
is_equal = x == y
is_divisible = y != 0 and x % y == 0

print("x greater than y:", is_greater)
print("x equal to y:", is_equal)
print("x divisible by y:", is_divisible)