import sys
from collections import deque

input = sys.stdin.readline

# 깊이 탐색 아니면 너비 탐색?

n = int(input())
arr = [[int(x) for x in input().strip()] for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[0] * n for _ in range(n)]

k = []
sum = 0

stack = deque()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] != 1:
            stack.append((i,j))
            visited[i][j] = 1
            number = 1

            while stack:
                # 꺼내기
                x, y = stack.pop()

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and visited[nx][ny] != 1:
                        visited[nx][ny] = 1
                        number += 1
                        stack.append((nx, ny))

            if number != 0:
                k.append(number)

k.sort()
print(len(k))
for x in k:
    print(x)
