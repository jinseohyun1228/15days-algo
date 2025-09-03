import sys
from collections import deque

input = sys.stdin.readline

# 깊이 탐색 아니면 너비 탐색?

n = int(input())

arr = [[int(x) for x in input().strip()] for _ in range(n)]


stack = deque()
visited = [[0] * n for _ in range(n)]

route = []

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if arr[i][j] == 1:
            route.append((i, j))

i, j = 0, 0


def get_index(i, j):
    global n
    candidates = [
        (i - 1, j),  # 위
        (i + 1, j),  # 아래
        (i, j - 1),  # 왼쪽
        (i, j + 1)  # 오른쪽
    ]
    # 유효한 범위만 필터링
    return [(x, y) for x, y in candidates if 0 <= x < n and 0 <= y < n]


k = []
sum = 0
max = len(route)

while sum < max:
    stack.append(route.pop())
    number = 0

    while stack:
        # 꺼내기
        i, j = stack.pop()
        # 방문 검사와 방문 표시
        if visited[i][j] == 1:
            continue
        visited[i][j] = 1
        number += 1
        sum += 1
        for s, e in get_index(i, j):
            if arr[s][e] == 1:
                stack.append((s, e))

    if number != 0:
        k.append(number)

k.sort()
print(len(k))
for x in k :
    print(x)
