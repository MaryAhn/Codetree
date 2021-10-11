obj = list(input())
tgt = list(input())
n1 = len(obj)
n2 = len(tgt)

# 첫 번째 시작을 공집합으로 간주하고 dp를 만든다.
dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
lcs = []

# 공집합과 문자열을 비교하면 문자열의 길이가 dp의 값이 된다.
for i in range(1, n1+1):
    dp[i][0] = i
for j in range(1, n2+1):
    dp[0][j] = j

# dp[i][j]: i번째와 j번째까지를 비교했을때의 edit distance
for i in range(1, n1+1):
    for j in range(1, n2+1):
        # 두 문자열의 끝이 같을 경우 연산을 할 필요가 없다. 따라서 이전의 값을 끌고 온다.
        if obj[i-1] == tgt[j-1]:
            dp[i][j] = dp[i-1][j-1]
        # 끝이 다를 경우
        # dp[i-1][j]: obj에서 하나를 삭제한 경우
        # dp[i][j-1]: tgt에서 문자를 하나 추가한 경우
        # dp[i-1][j-1]: 두 문자열이 같다고 보는 것, 즉 교체의 경우
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
for i in range(n1):
    print(dp[i])

print(dp[n1][n2])


