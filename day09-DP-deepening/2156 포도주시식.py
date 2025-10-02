import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i < 2:
        dp[i][1] = 0 + arr[i - 1]
    else:
        dp[i][1] = dp[i - 2][0] + arr[i - 1]
    dp[i][2] = dp[i - 1][1] + arr[i - 1]
    dp[i][0] = max(dp[i][1], dp[i][2], dp[i-1][0])


print(dp[-1][0])
