import sys

input = sys.stdin.readline

INF = 10 ** 13

n, k = map(int, input().split())
c = {int(input()) for _ in range(n)}

c = list(c)

n = len(c)

dp = [[INF] * (k + 1) for _ in range(n)]

# 첫번째 열 !
i = 0

for w in range(k + 1):
    if w == c[i]:
        dp[i][w] = 1
    elif w > c[i] and w % c[i] == 0:
        dp[i][w] = 1 + dp[i][w - c[i]]

for i in range(1, n):
    for w in range(k + 1):
        if w == c[i]:
            dp[i][w] = 1
        elif w > c[i]:
            dp[i][w] = min(dp[i][w - c[i]] + 1, dp[i - 1][w])

if dp[-1][-1] == INF:
    print(-1)
else:
    print(dp[-1][-1])
