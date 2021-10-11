weight = [3, 1, 4, 5, 2]
price = [4, 1, 2, 6, 3]
n = int(input())
dp = [[-1 for _ in range(n+1)] for _ in range(5)]

dp[0][0] = 0
dp[0][weight[0]] = price[0]

for i in range(1, 5):
    for j in range(n+1):
        if j - weight[i] >= 0 and dp[i-1][j-weight[i]] != -1:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + price[i])
        else:
            dp[i][j] = dp[i-1][j]
for i in range(5):
    print(dp[i])