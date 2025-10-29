import sys
import heapq
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

gem = [ [int(x) for x in input().split()] for _ in range(n)]
bag = [int(input()) for _ in range(k)]

gem.sort()
gem = deque(gem)
bag.sort()

pq = []
result = 0
for i in bag:
    while gem and gem[0][0] <= i :
        heapq.heappush(pq,-gem[0][1])
        gem.popleft()
    if pq:
        result -= heapq.heappop(pq)

print(result)