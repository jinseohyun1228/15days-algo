import sys

input = sys.stdin.readline

x = int(input())


dp = [0] * (x + 1)

for i in range(1,4):
    if i > x :
        break
    if i == 1 :
        dp[i] = 0
    else :
        dp[i] = 1

for i in range(4,x + 1):

    # 3가지의 경우
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i//3] + 1,dp[i//2] + 1,dp[i-1] + 1)
    elif i % 2 == 0:
        dp[i] = min( dp[i // 2] + 1, dp[i - 1] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
    else :
        dp[i] = dp[i - 1] + 1

print(dp[x])