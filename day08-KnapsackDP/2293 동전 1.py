import sys

input = sys.stdin.readline

n, k = map(int, input().split())

c = [int(input()) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(2)]

dp[0][0] = 1
dp[1][0] = 1

for w in range(1, k + 1):
    if w >= c[0] and w % c[0] == 0:
        dp[0][w] = 1

for i in range(1, n):
    for w in range(k + 1):
        if i % 2 == 0 :
            if w < c[i]:
                dp[0][w] = dp[1][w]
                continue
            dp[0][w] = dp[1][w] + dp[0][w - c[i]]

        else :
            if w < c[i]:
                dp[1][w] = dp[0][w]
                continue
            dp[1][w] = dp[0][w] + dp[1][w - c[i]]

if (n-1) % 2 == 0 :
    print(dp[0][-1])
else :
    print(dp[1][-1])
