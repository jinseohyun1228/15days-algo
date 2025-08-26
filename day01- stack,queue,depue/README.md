# 2일차 스택, 큐, 덱
### 들어가면서
```
오늘은 코테의 기본 문법인 스택, 큐, 덱의 파이썬 문법을 배우고 관련된 기본 문제들을 풀어봅시다! 

- 학습 알고리즘: 스택, 큐, 덱
- 학습 방법: 자료구조별 동작 방식 직접 구현해보기, 응용 문제로 패턴 익히기
- 풀어야할 문제:
	❎ 1874 스택 수열 (실패! -> 주말에 ㄱㄱ)
	✅ 9012 괄호
	✅ 2493 탑
	✅ 5430 AC 
```

## 스택
- `선입 후출 : 나중에 들어온게 제일 먼저나간다.`
- 스택은 뒤에서 꺼내면 되기 때문에 `list`로 사용해도 충분하다.
```py
stack = []
stack.append(x) → 삽입 (push)
stack.pop() → 삭제 (pop, 마지막 원소 반환)
stack[-1] → top 확인
not stack → 비었는지 확인
```

## 큐 
- `선입 선출 : 제일 먼저 들어온게 제일 먼저 나간다.`
- 리스트로 사용하면 앞에서 꺼내는 동작이 `O(n)`이라서 비효율적이다. 따라서 `dequeue`	를 쓴다.


```py
from collections import deque
queue = deque()

queue.append(x) → 삽입 (뒤에 추가)
queue.popleft() → 삭제 (앞에서 꺼냄)
queue[0] → front 확인
not queue → 비었는지 확인
```


## 덱
- Deque는 양쪽 끝에서 삽입/삭제가 모두 가능하다. 따라서 큐를 쓸 떄 사용한다 ~! 

```py
from collections import deque
dq = deque()

dq.append(x) → 오른쪽 삽입
dq.appendleft(x) → 왼쪽 삽입
dq.pop() → 오른쪽 삭제  =>  스택
dq.popleft() → 왼쪽 삭제 => 큐!!
dq[0], dq[-1] → 양 끝 원소 확인
```

## 실제 문제 풀이
#### 9012 괄호
- 풀이 링크 : [🔗 개인 노션 링크]
- 한줄 정리 :`print("\n".join(r))` -  리스트를 여러줄로 간단히 출력하는 방법
![](https://velog.velcdn.com/images/sseohyun_0v0/post/96245348-2c1f-45b4-a36c-3fef920086b6/image.png)


#### 5430_AC
- 풀이 링크 : [🔗 개인 노션 링크](https://www.notion.so/AC-25ba610cc38780058d3ed6d01c0bd1d0)
- 한줄 정리 :`-1/1` 사용하기 간단 !
![](https://velog.velcdn.com/images/sseohyun_0v0/post/4a1515ef-89fa-48af-a739-9ad455f51a93/image.png)


#### 2493_탑
- 풀이 링크 : [🔗 개인 노션 링크](https://www.notion.so/25ba610cc3878007ae96c4c74fa700e8)
- 한줄 정리 : 형변환에 신경쓰자 
![](https://velog.velcdn.com/images/sseohyun_0v0/post/e6d978e0-69eb-477a-96ac-0627dd4f5404/image.png)

### 마무리하면서 
```
원래 2일차가 제일 힘들다. 
이정도면 만족 !! 아주 잘했어 !! 

생각 안나는 스택 수열은 주말로 미뤄서 이번주 내로 설명하면 굿굿 그자체 !! 

오랜만에 dequeue 문법도 정리해서 아주 좋았음 !! 굿굿

pop(), popleft() 기억하자!!
```

