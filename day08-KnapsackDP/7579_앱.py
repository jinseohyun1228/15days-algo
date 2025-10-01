import sys
input = sys.stdin.readline

INF = 10 ** 13


n, b = map(int,input().split()) #앱 개수

#qkdlxm
app_b = [int(x) for x in input().split()]
app_c = [int(x) for x in input().split()]

# ⭐️️️️⭐️️️️⭐️️️️⭐️️️️⭐️️️️ 왜 비용을 0부터 고려하니까, 배열 길이 특성상 um(app_c) 도 포함할려면 sum(app_c) + 1
len_c = sum(app_c) + 1
dp = [ [0] * len_c for _ in range(n) ]

i = 0

# 해당 요소는 뭐라고 할 수 있을까?
# dp[물건 번호][비용] : 헤당물건까지 고려했을 때, 비용으로 끌 수 있는 최대 바이트 !!!
# 이후 어떻게 활용??
# -> 마지막 행을 순회회하면서 필요 바이트를 넘는 비용중 제일 최소 값을 선택..!


dp[i][app_c[i]] = app_b[i]

for i in range(1,n) :
    for c in range(len_c) :
        # 물건 비용이 현재 고려 비용 보다 큰 경우?
        if app_c[i] > c :
            dp[i][c] =dp[i-1][c]
        else :
            dp[i][c] = max(dp[i - 1][c],dp[i - 1][c - app_c[i]] + app_b[i])

min_v = INF

for c in range(len_c) :
    if dp[-1][c] >= b :
        min_v = min(min_v,c)

print(min_v)