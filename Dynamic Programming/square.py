dp = [[0 for _ in range(8)] for _ in range(8)]
org = [[0 for _ in range(8)] for _ in range(8)]

for i in range(8):
    tmp = input().split()
    for j in range(8):
        org[i][j] = int(tmp[j])


for i in range(8):
    for j in range(8):
        dp[i][j] = max(dp[i][j-1] + org[i][j], dp[i-1][j] + org[i][j])

print(dp[7][7])