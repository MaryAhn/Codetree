num = input()
nums = num.split()
n = len(nums)
dp = [1 for _ in range(n)]

for i in range(n):
    nums[i] = (int)(nums[i])

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(dp)