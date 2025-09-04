import sys
# collections
from collections import deque

input = sys.stdin.readline

case = int(input())
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
result = [0] * case

for i in range(case):
    n, m, k = map(int, input().split())
    # dict = {(x,y) : 0 for x,y in map(int,input().split()) for_ in range(k) }
    d = {tuple(map(int, input().split())): 0 for _ in range(k)}

    queue = deque()

    number = 0

    for key, v in d.items():
        if v == 1:
            continue
        d[key] = 1
        number += 1
        queue.append(key)

        while queue:
            x, y = queue.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx,ny) in d and d[(nx,ny)] == 0:
                    d[(nx, ny)] = 1
                    queue.append((nx, ny))

    result[i] = number

for x in result:
    print(x)