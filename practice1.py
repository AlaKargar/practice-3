import random

n = int(input())
nums = []
while len(nums) < n:
    x = random.randint(0, 20)
    if x not in nums:
        nums.append()

print(nums)
