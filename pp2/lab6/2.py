n = int(input())
a = list(map(int, input().split()))

nums = list(filter(lambda x: x % 2 == 0, a))

print(len(nums))   