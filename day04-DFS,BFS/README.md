# 그래프 탐색 기초 : DFS, BFS 

### 학습 목표
```
✅ 인접리스트/행렬 구현
✅ 재귀 DFS vs 큐 BFS 비교
```

## DFS 
- 핵심 포인트: 깊게! 갈 수 있을 때까지 끝까지 들어가고, 막히면 뒤로 돌아옴.
- 구현 방법:
  - 재귀 구현 (스택 원리)
  - 스택 자료구조 사용
- 특징:
경로 추적, 백트래킹, 경우의 수 탐색에 적합
방문 순서가 한쪽으로 쭉 뻗어나가는 느낌

### 구현 코드
```py
from collections import deque

# 예시 그래프 (인접 리스트)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

# ----------------
# DFS (재귀)
# ----------------
def dfs_recursive(v, visited):
    visited.add(v)
    do_something(v)  # <- 여기서 노드 방문 시 원하는 동작
    print(v, end=" ")
    for nxt in graph[v]:  # 연결된 리스트 탐색 
        if nxt not in visited: # 해당 노드를 방문하지 않았을 경우
            dfs_recursive(nxt, visited)

# ----------------
# DFS (스택)
# ----------------
def dfs_stack(start):
    visited = set()
    stack = [start]
    while stack:  # 비어질때까지
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            print(v, end=" ")
            # 역순으로 넣어야 작은 번호 먼저 방문 가능
            stack.extend(graph[v])

```

### 왜 DFS는 스택을 쓰고, 왜 BFS에서는 큐를 쓸 까
DFS는 깊이 우선 탐색이고, BFS는 너비 우선 탐색이다.
 
DFS는 깊이가 끝인, 더 탐색할게 없는 리스트에 갈때까지 탐색한다. 
그러다보니 동일 뎁스에 있는 다른 리스트가 있더라도, 내가 탐색하는 리스트의 하위 리스트를 먼저 가야한다. 
해당 상황을 실제 스택의 상태로 설명해보자

```py
1. 노드 A를 탐색하기 시작 : [(이전 뎁스 노드), ... ,(동일 뎁스 노드)] -> 노드 A를 맨 뒤에서 꺼냄
2. 노드 A에 연결된 하위 노드의 리스트 : graph[A] = [a,b,c]

3. 하위 노드 담기 동작 후 : [(이전 뎁스 노드), ... ,(동일 뎁스 노드), a, b, c]  
```
이후 탐색할 노드에 접근하기 위해서는, 방금 전에 들어온 노드를 꺼내는 선입 후출의 스택이 필요하다. 앞에서 꺼내면, 하위 노드가 아닌 엉뚱한 노드를 탐색하게 된다. 반대로 동일 뎁스의 노드에 접근해야하는 bfs는 선입 선출의 큐를 쓰는 것이다.

또한, DFS의 자료구조때문에 노드 순서가 반전된다는 것을 유의하자, 

 


## BFS 
- 핵심 포인트: 넓게! 시작점에서 가까운 노드부터 탐색.
- 구현 방법:
	- 큐(Queue) 사용 (FIFO 원리)
- 특징:
최단 거리 문제에 자주 사용 (특히 간선 가중치가 1일 때)
방문 순서가 동심원처럼 퍼져나가는 느낌

### 구현 코드
```py
from collections import deque

# 예시 그래프 (인접 리스트)
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}


# ----------------
# BFS (큐)
# ----------------
def bfs(start):
    visited = set([start])
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for nxt in graph[v]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)

```
## 인접 행렬 vs 인접 리스트
인접 행렬: 2차원 배열, graph[a][b] = 1 이면 연결됨.
- 장점: 구현 간단, 연결 여부 확인 O(1)
- 단점: 메모리 많이 차지 (O(N²))

인접 리스트: 각 노드마다 연결된 노드를 리스트로 저장.
- 장점: 메모리 절약 (O(N+E))
- 단점: 특정 연결 여부 확인은 느림

## 재귀 DFS vs 큐 BFS 비교

| 구분    | DFS             | BFS                    |
| ------- | --------------- | ---------------------- |
| 탐색 방식 | 깊게 들어감        | 가까운 노드부터             |
| 자료구조  | 스택(재귀)        | 큐                       |
| 활용    | 경로 탐색, 백트래킹 | 최단 거리, 레벨 탐색         |
| 속도    | 경우에 따라 빠름, 최단 거리 보장은 없음 | 간선이 균일하면 최단 거리 보장 |


❗️_간선이 동일하다는 것의 의미_ : 노드간의 거리가 모두 1로 동일
-> 따라서 이 경우에는 BFS에서 어떤 노드에 처음 도달한 순간이 곧 최단 거리임을 보장

## 실제 문제 풀어보기

#### 1260 DFS와 BFS
- 풀이 링크 : [🔗 개인 노션 링크](https://www.notion.so/DFS-BFS-262a610cc387806c9522c0c0a712c202)
- 한줄 정리 : 숫자리스트요소를 공백구분해서 한줄 출력 `print(" ".join(map(str, bfs)))`  
![](https://velog.velcdn.com/images/sseohyun_0v0/post/b4e0baeb-6cbf-45d8-ba93-05e19b4be2ad/image.png)

#### 2606 바이러스
- 풀이 링크 : [🔗 개인 노션 링크](https://www.notion.so/262a610cc387801c99d9eeb24476f493)
- 한줄 정리 : 굿 ^_^ 
![](https://velog.velcdn.com/images/sseohyun_0v0/post/1082a5b7-e4a9-480d-8382-d38f6f57d292/image.png)

#### 2667 단지 번호 붙이기
- 풀이 링크 : [🔗 개인 노션 링크](https://www.notion.so/262a610cc38780599519cb54c1a2ac91)
![](https://velog.velcdn.com/images/sseohyun_0v0/post/1ce7918c-d3a5-459c-b1e8-4d5a01b52ebe/image.png)

#### 2178 미로탐색
- 풀이 링크 : [🔗 개인 노션 링크](https://opalescent-leaf-e7c.notion.site/262a610cc387807ea86be59313b2f4e2?pvs=74)
- 한줄 정리 :  **기준인덱스의 유효한 상하좌우 좌표 구하기**
  ```python
    #외부에서 좌표 설정
    dirs = [(-1,0),(1,0),(0,-1),(0,1)] 
    
    #상대 좌표
    for dx, dy in dirs:
      #절대 좌표로 변경
      nx, ny = x + dx, y + dy
      
      #절대 좌표의 유효성 검사
      if 0 <= nx < n and 0 <= ny < n \
         and grid[nx][ny] == 1 and not visited[nx][ny]:
          # 원하는 동작

  ```
![](https://velog.velcdn.com/images/sseohyun_0v0/post/1ce7918c-d3a5-459c-b1e8-4d5a01b52ebe/image.png)

### 단지번호붙이기의 더 좋은 코드
#### 기존 코드의 문제 
1.  **불필요한 `route` 사용** 
    
    차례대로 순회해도 동일 
    
2. **`get_index` 라는 함수 불필요** 
    
    ```python
    #외부에서 좌표 설정
    dirs = [(-1,0),(1,0),(0,-1),(0,1)] 
    
    #상대 좌표
    for dx, dy in dirs:
      #절대 좌표로 변경
      nx, ny = x + dx, y + dy
      
      #절대 좌표의 유효성 검사
      if 0 <= nx < n and 0 <= ny < n \
         and grid[nx][ny] == 1 and not visited[nx][ny]:
          # 원하는 동작
    ```
    
#### 개선코드 : 내부에서 방문 표시
```py
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
            stack.append((i, j))
            number = 0

            while stack:
                # 꺼내기
                x, y = stack.pop()
                # 방문 검사와 방문 표시
                if visited[x][y] == 1:
                    continue
                visited[x][y] = 1
                number += 1
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                        stack.append((nx, ny))

            if number != 0:
                k.append(number)

k.sort()
print(len(k))
for x in k:
    print(x)

```
#### 개선코드 : `push` 전에 방문 검사  
```py
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

```
