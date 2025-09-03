import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
t = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

v = []

stack = deque()
stack.append(1)

while stack:
    n = stack.pop()
    if n not in v:
        v.append(n)
        stack.extend(graph[n])

print(len(v) - 1)
