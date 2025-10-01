import sys

input = sys.stdin.readline

INF = 10 ** 13

n, k = map(int, input().split())
c = {int(input()) for _ in range(n)}

c = list(c)

n = len(c)

dp = [INF] * (k + 1)

# 첫번째 열 !
i = 0

for w in range(k + 1):
    if w == c[i]:
        dp[w] = 1
    elif w > c[i] and w % c[i] == 0:
        dp[w] = 1 +dp[w - c[i]]

for i in range(1, n):
    for w in range(k + 1):
        if w == c[i]:
            dp[w] = min(1, dp[w])
        elif w > c[i]:
            dp[w] = min(dp[w - c[i]] + 1, dp[w])

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
