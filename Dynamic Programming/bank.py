coin = [1, 4, 5, 9]
n = int(input())
dp = [22 for _ in range(n+1)]
dp[0] = 0

for i in range(n+1):
    for j in range(len(coin)):
        if i - coin[j] >= 0:
            dp[i] = min(dp[i], dp[i-coin[j]] + 1)

print(dp)