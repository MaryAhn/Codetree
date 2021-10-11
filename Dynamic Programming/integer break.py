# leetcode interger break problem https://leetcode.com/problems/integer-break/

n = int(input())
dp = [0 for _ in range(n+1)]

for i in range(n + 1):
    if i == 1:
        dp[i] = 1
    else:
        # print(i)
        for j in range(i+1):
            dp[i] = max(dp[i], dp[i-j] * j, (i-j) * j)

print(dp)