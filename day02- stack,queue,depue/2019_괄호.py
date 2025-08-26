import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

str_list = [input().strip() for _ in range(n)]
r = ["YES"] * n


for i,str in enumerate(str_list):
    dq = deque()
    for s in str :
        if s == "(":
            dq.append(s)
        elif s == ")":
            if not dq: # 비어있을 때
                r[i] = "NO"
                break
            elif dq.pop() != "(":
                r[i] = "NO"
                break
    if dq :
        r[i] = "NO"

print("\n".join(r))