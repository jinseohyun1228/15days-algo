import sys
from collections import deque

intput = sys.stdin.readline

n, m = map(int, input().split())

arr = [[int(x) for x in input().strip()] for _ in range(n)]

queue = deque()
visited = [[0] * m for _ in range(n)]


def get_index(i, j):
    global n
    global m

    candidates = [
        (i - 1, j),  # 위
        (i + 1, j),  # 아래
        (i, j - 1),  # 왼쪽
        (i, j + 1)  # 오른쪽
    ]
    # 유효한 범위만 필터링
    return [(x, y) for x, y in candidates if 0 <= x < n and 0 <= y < m]


# 시작하기

queue.append((0, 0, 1))

while queue:
    i, j, d = queue.popleft()
    if visited[i][j] == 1:
        continue
    visited[i][j] = 1
    if (i, j) == (n - 1, m - 1):
        print(d)
        break
    for s, e in get_index(i, j):
        if arr[s][e] == 1:
            queue.append((s, e, d + 1))
