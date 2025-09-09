import sys

input = sys.stdin.readline


n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [[0,0,0] for _ in range(n)]

dp[0][1] =  stairs[0]
dp[0][2] =  stairs[0]

for i in range(1,n) :
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = dp[i - 1][0] + stairs[i]
    dp[i][2] = dp[i - 1][1] + stairs[i]

print(max(dp[-1][1],dp[-1][2]))


