import sys
input = sys.stdin.readline

n = int(input())
arr = [int(x) for x in input().split()]

dp = [0] * n

result = 0

for i in range(n) :
    m = 0
    for j in range(i-1, -1,-1) :
        if arr[j] < arr[i] :
            # dp[j] 가 아니라 dp[i]로 해버림
            m = max(m,dp[j])
    dp[i] = m + 1
    result = max(result,dp[i])

print(result)
