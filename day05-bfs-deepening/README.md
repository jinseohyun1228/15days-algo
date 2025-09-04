

# BFS 심화
### 학습 목표
```
✅ 다중 시작점 BFS
✅ 최단거리 응용
// 숨바꼭질 미해결 9월 6~7일 중 해결 예정 
```
## 다중 시작점 BFS
- **개념** : 일반 BFS는 보통 시작점이 하나이지만
다중 시작점 BFS는 시작점이 여러 개일 때, 모두 동시에 출발시키는 방식이다.
- **구현** : 단순히 여러개인 시작점 모두를 큐에 집어넣고 시작하면 된다.
- **이점**: 동시에 시작하기 때문에 시작점이 여러개 일때 **모든 시작점으로부터의 최소 거리**를 구하기 쉽다. 


## 최단거리 응용
- **개념** : BFS는 간선 가중치가 동일할 때 최단거리를 보장한다. 또한 단순 최단거리뿐 아니라, 특정 레벨까지만 탐색이나 탐색하면서 상태(조건)를 함께 고려같은 확장이 가능
- **거리 계산** : `dist[next] = dist[curr] + 1` 로 거리 배열을 관리


#### 거리 계산방법 
저번 미로 찾기 문제에서는 거리를 방문 큐에 같이 저장하면서 활용했다.

	queue.append((i, j, d+1))

만약 각 지점 별 거리를 활용해야한다면 별도의 거리 배열을 만들어서 사용할 수 있다.
	
    dist[next] = dist[curr] + 1


## 문제 풀기
#### 7576 토마토
- 풀이 링크 : [🔗 개인 노션 링크](https://www.notion.so/263a610cc387801d8308f39bc7e97e2a)
- 한줄 정리 : 토마토 개수를 세서, 토마토를 찾을때마다 -1 연산해주기
![](https://velog.velcdn.com/images/sseohyun_0v0/post/03b40f6f-ed33-4f49-91ce-37b5b3f8ea2e/image.png)

#### 1012 유기농 배추
- 풀이 링크 : [🔗 개인 노션 링크](https://www.notion.so/263a610cc387805baa5eec6ba0af0c03)
- 한줄 정리 : 배추 밭 배열을 별도로 만들지 않고 바로 dict으로 만들었다. 배추밭배열을 만드면 n * m 배열을 무조건 순회해야하는데 이 코드에서는 그런 반복문이 빠져서 시간이 많이 단축된 것 같다 !! ^_^ 이번 기회에 dict도 한번 더 정리해봣어요 
![](https://velog.velcdn.com/images/sseohyun_0v0/post/015fa282-d6b8-4754-9c71-91a079bb828b/image.png)


#### 11724 연결요소의 개수
- 풀이 링크 : [🔗 개인 노션 링크](https://www.notion.so/263a610cc38780aab1dcc51226812e2a)
- 한줄 정리 : 양방향 그래프 만들기
![](https://velog.velcdn.com/images/sseohyun_0v0/post/d4531399-8ce3-494f-abd1-1b1df65b1c1e/image.png)


## 추가 정리) 파이썬 dict

```python
d = {"a": 1, "b": 2}

# 안전한 조회
d.get("a", 0)       # key 없으면 0 반환

# key, value 순회
for k, v in d.items():
    ...

# 다른 dict 합치기 / 값 갱신
d.update({"b": 3, "c": 4})

# key 삭제 & 값 반환
d.pop("a", 0)       # 없으면 기본값 반환

# 전체 삭제
d.clear()

# key / value만 보기
d.keys()
d.values()
```