import sys

input = sys.stdin.readline

n, m = map(int, input().split())

t = [int(x) for x in input().split()]

l = 0
r = max(t) + 1

mid = 0

while l < r:
    mid = (l + r) // 2
    result = 0

    for tree in t:
        result += max(0, tree - mid)

    if result < m:  # 처음으로 불가능한 false를 찾는다.
        r = mid
    else: # result >= m : 조건 만족, 해당 범위를 제외하고 false를 찾는다. ( 시작을 높여야한다.)
        l = mid + 1


print(r - 1)
