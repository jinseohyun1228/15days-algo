import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
arr = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0] * m for _ in range(n)]

h = []

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp[0][0] = 1
visited[0][0] = 1

heapq.heappush(h, (-arr[0][0], 0, 0))

while h:
    v, i, j = heapq.heappop(h)

    for x, y in dirs:
        dx = i + x
        dy = j + y
        if 0 <= dx < n and 0 <= dy < m:
            if arr[dx][dy] < arr[i][j] and visited[dx][dy] != 1:
                visited[dx][dy] = 1
                heapq.heappush(h, (-arr[dx][dy], dx, dy))
            elif arr[dx][dy] > arr[i][j]:
                dp[i][j] += dp[dx][dy]


    if i == n - 1 and j == m - 1:
        break

print(dp[n-1][m-1])
