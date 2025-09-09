import sys
input = sys.stdin.readline

t = int(input())

arr = [0] * t
m = 0
for i in range(t) :
    arr[i] = int(input())
    m = max(m,arr[i])

if m + 1 > 4 :
    dp = [0] * (m + 1)
else :
    dp = [0] * 4

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,m + 1) :
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in arr :
    print(dp[i])
