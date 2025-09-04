import sys
from collections import deque

input = sys.stdin.readline

s, e = map(int, input().split())

queue = deque()

queue.append((e, 0))

while queue:
    e, d = queue.popleft()
    if e == s:
        print(d)
        break
    else:
        queue.append((e + 1, d + 1))
        queue.append((e - 1, d + 1))
        if e % 2 == 0:
            queue.append((e // 2, d + 1))



