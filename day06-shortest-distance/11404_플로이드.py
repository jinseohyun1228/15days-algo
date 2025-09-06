import sys
import heapq

input = sys.stdin.readline
INF = 10 ** 11

n = int(input())
m = int(input())
n += 1

# 인접 그래프 만들지 않아도 되지 않을까요
dist = [[INF] * n for _ in range(n)]

for _ in range(m):
    s, e, w = map(int, input().split())
    dist[s][e] = min(dist[s][e], w)


for k in range(1, n):
    for i in range(1, n):
        for j in range(1, n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    dist[k][k] = 0

for k in range(1, n):
    for x in dist[k][1::] :
        if x == INF :
            print(0,end= " ")
        else:
            print(x,end= " ")
    print()