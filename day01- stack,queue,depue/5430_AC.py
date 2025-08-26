import sys
import json
from collections import deque


input = sys.stdin.readline

t = int(input())
f = []
l = []
r = []
queue = deque()


for _ in range(t):
    f.append(input().strip())
    l.append(input().strip())
    queue.append(deque(json.loads(input().strip())))

for i in range(t):
    d = 1
    for s in f[i]:
        if s == "R" :
            d *= -1
        elif s == "D" and queue[i]:
            if d == 1 :
                queue[i].popleft()
            else :
                queue[i].pop()
        else :
            queue[i] = "error"
            break
    if queue[i] != "error" and d == -1 :
        queue[i].reverse()



for x in queue:
    if x == "error":
        print(x)
    else:
        print(str(list(x)).replace(" ", ""))