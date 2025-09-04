import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

t = [[int(x) for x in input().split()] for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0] * m for _ in range(n)]

queue = deque()
day = 0
sum = 0
zero  = 0
temp = []
# 시작 티비!

for i in range(n):
    for j in range(m):
        if t[i][j] == 1:
            visited[i][j] = 1
            temp.append((i, j))
        elif t[i][j] == 0 :
            zero += 1

sum += len(temp)
queue.append(temp)

# 모든 토마토가 이미 익어있다면
if zero == 0:
    print(0)
    sys.exit()


while queue:
    temp = []

    for i,j in queue.popleft():
        for dx, dy in dirs:
            nx, ny = i + dx, j + dy
            # 조건식
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1:
                if t[nx][ny] == 0 : #있는 친구
                    visited[nx][ny] = 1
                    zero -= 1
                    temp.append((nx, ny))
                    sum += 1


    if temp:
        day += 1
        queue.append(temp)

if zero != 0 :
    print(-1)
    sys.exit()
print(day)
