n = int(input())
dp = [0 for i in range(n+1)]
nums = [1, 2, 3, 4]
dp[0] = 1

for i in range(5, n+1):
    for num in nums:
        if i - num >= 0:
            dp[i] += dp[i - num]

print(dp)