str1 = list(input())
str2 = list(input())

n1 = len(str1)
n2 = len(str2)

dp = [[0 for _ in range(n2)] for _ in range(n1)]

for i in range(n2):
    if str1[0] == str2[i]:
        dp[0][i:] = [1] * (n2 - i)
        break
for j in range(n1):
    if str2[0] == str1[j]:
        for k in range(j, n1):
            dp[k][0] = 1
        break

for i in range(1, n1):
    for j in range(1, n2):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

for i in range(n1):
    print(dp[i])