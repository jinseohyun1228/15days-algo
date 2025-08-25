import sys
input = sys.stdin.readline

n = int(input())
m = [[int(x) for x in input().split()] for _ in range(n)]


m.sort()
s = 1
prev = m[0]

#  정렬을 통해 무조건 curr는 prev보다 늦게 시작하는 거 보장
for curr in m[1:] :
    #일단은 선택가능
    if prev[1] <= curr[0]:
        s += 1
        prev = curr
    elif curr[1] < prev[1]:
        prev = curr # 오타

print(s)