n = int(input())
dp = [0 for i in range(n+1)]
nums = [1, 2, 3, 4]
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 8

# 4는 단독으로 표현되지 않기 때문에 base를 4까지 넣어줘야 한다.

for i in range(5, n+1):
    for num in nums:
        if i - num >= 0:
            dp[i] += dp[i - num]

print(dp)