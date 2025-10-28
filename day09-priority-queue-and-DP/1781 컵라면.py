import heapq
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
pq = []
result = 0

q = [[int(x) for x in input().split()] for _ in range(n)]
q.sort(reverse = True)
q = deque(q)

for i in range(n, 0, -1):
    while q and q[0][0] >= i:
        heapq.heappush(pq, -q[0][1])
        q.popleft()
    if pq :
        result -= heapq.heappop(pq)

print(result)
