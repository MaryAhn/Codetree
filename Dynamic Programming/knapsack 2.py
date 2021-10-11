weight = [2, 6, 2, 3, 4, 5, 4, 6, 7, 10]
price = [3, 5, 4, 2, 3, 3, 2, 6, 9, 8]
n = int(input())
dp = [[-1 for _ in range(n+1)] for _ in range(10)]

dp[0][0] = 0
dp[0][weight[0]] = price[0]

for i in range(1, 10):
    for j in range(n+1):
        if j - weight[i] >= 0 and dp[i-1][j-weight[i]] != -1:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + price[i])
        else:
            dp[i][j] = dp[i-1][j]
for i in range(10):
    print(dp[i])