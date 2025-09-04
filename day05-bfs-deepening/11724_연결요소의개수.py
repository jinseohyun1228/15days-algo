import sys
# collections
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

# 그래프 만들기
for _ in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

stack = deque()
number = 0

for i in range(1,n+1):
    if visited[i] == 1 :
        continue
    visited[i] = 1
    stack.append(i)
    number += 1

    while stack:
        v = stack.pop()
        for u in graph[v] :
            if visited[u] == 0 :
                visited[u] = 1
                stack.append(u)

print(number)



