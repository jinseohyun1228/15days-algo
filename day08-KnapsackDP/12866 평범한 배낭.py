import sys

input = sys.stdin.readline

n, k = map(int, input().split())

st = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n)]

# 첫번째 물건 담기
i = 0

for w in range(0,k+1) :
    if w >= st[i][0] : #물건을 넣을 수 있을 때만 고려
        dp[i][w] = max(0,st[i][1])

for i in range(1, n):
    for w in range(0, k + 1):
        if w >= st[i][0]:  # 물건을 넣을 수 있을 때만 고려
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - st[i][0]] + st[i][1])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[-1][-1])