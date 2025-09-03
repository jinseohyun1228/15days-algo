import sys
from collections import deque

stack = deque()
queue = deque()

input = sys.stdin.readline

n,m,start = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)


# graph.sort() => 전체 리스트 정렬이 되어버린다 (인데스 기준 연결 리스트 위치가 바뀜)

for i in range(1, n+1):
    graph[i].sort()

dfs = []
bfs = []

stack.append(start)

v_s = [0] * (n+1)

while stack :
    v = stack.pop()
    if v_s[v] == 0 : # 미방문일때
        v_s[v] = 1
        dfs.append(v)
        stack.extend(reversed(graph[v]))

print(" ".join(map(str, dfs)))


queue.append(start)
v_q = [0] * (n+1)

while queue:
    v = queue.popleft()
    if v_q[v] == 0 : # 미방문일때
        v_q[v] = 1
        bfs.append(v)
        queue.extend(graph[v])

print(" ".join(map(str, bfs)))