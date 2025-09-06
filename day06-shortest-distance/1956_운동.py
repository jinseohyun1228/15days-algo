import sys
import heapq

input = sys.stdin.readline

INF = 10 ** 12
v , e = map(int,input().split())

v+= 1

dist = [ [INF] * v for _ in range(v)]

for _ in range(e):
    s,e,d = map(int,input().split())
    dist[s][e] = d

result= INF

for k in range(1,v):
    for i in range(1,v):
        for j in range(1,v):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            if i == j :
                result= min(dist[i][j],result)

if result == INF:
    result = -1
print(result)