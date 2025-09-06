import sys
import heapq

input = sys.stdin.readline

INF = 10 ** 11

v, e = map(int,input().split())
v += 1

start = int(input())
temp = [tuple(map(int,input().split())) for _ in range(e)]
visited = [0] * v
dist = [{} for _ in range(v)]

h = []
dp = [INF] * v

# 인접 그래프 형식으로 다시 바꾸자용
for s,e,w in temp :
    # 없는 경우
    if e not in dist[s] :
        dist[s][e] = w
    # 있는 경우
    else :
        dist[s][e] = min(dist[s][e],w) #최소 거리만 남기기

    if s == start :
        dp[e] =dist[s][e]
        heapq.heappush(h, (dist[s][e],e))

dp[start] = 0
visited[start] = 1

while h :
    #거리, 노드
    d,u = heapq.heappop(h)
    if visited[u] == 1 :
        continue
    visited[u] = 1

    for e,w in dist[u].items() :
        if dp[e] > dp[u] + w :
            dp[e] = dp[u] + w
            heapq.heappush(h, (dp[e], e))

for i in range(1, v):
    if dp[i] == INF :
        print("INF")
    else:
        print(dp[i])




