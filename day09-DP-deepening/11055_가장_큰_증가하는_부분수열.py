import sys
input = sys.stdin.readline

n = int(input())
arr = [int(x) for x in input().split()]
dp = [0] * n

result = 0
for i in range(n) :
    m = 0
    for j in range(i-1, -1 , -1) :
        if arr[j] < arr[i]:
            m = max(m, dp[j])
    dp[i] = m + arr[i]
    result = max(result, dp[i])

print(result)
