import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
j = [[int(x) for x in input().split()] for _ in range(n)]
b = [int(input()) for _ in range(k)]

j.sort()  # -> 가장 무거운 애부터
b.sort()  # 가장 조금 밖에 못넣는 애부터
s = 0
hq = []
i = 0
for x in b :
    while i < n and j[i][0] <= x :
        heapq.heappush(hq, -j[i][1])
        i += 1
    if hq:
        s += - heapq.heappop(hq)

print(s)