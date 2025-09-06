import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

#     d = {tuple(map(int, input().split())): 0 for _ in range(k)}
b = [tuple(map(int, input().split())) for _ in range(m)]

start, end = map(int, input().split())
INF = 10 ** 12

dist = [[INF] * (n+1) for _ in range(n+1)]

for s, e, d in b:
    dist[s][e] = min(d,dist[s][e])

dp = [INF] * (n+1)
visited = [0] * (n+1)

h = []

#dp 배열 만들기
for i in range(1, n+1):
    dist[i][i] = 0
    dp[i] = dist[start][i]
    if dp[i] < INF :
        heapq.heappush(h, (dist[start][i], i))  # 거리, 노드

while h:
    # 현재 최소 거리인 !!
    d, v = heapq.heappop(h)
    if visited[v] == 1:
        continue
    visited[v] = 1

    if v == end :
        break

    for u in range(1, n+1):
        if dist[v][u] == INF:
            continue
        if dp[v] + dist[v][u] < dp[u]:
            dp[u] = dp[v] + dist[v][u]
        heapq.heappush(h, (dp[u], u))


print(dp[end])
