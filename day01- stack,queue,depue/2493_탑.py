import sys

#  sys.stdin.readline
input = sys.stdin.readline

n = int(input())
t = [(int(x), i + 1) for i, x in enumerate(input().split())]

st = []
r = []

for v in t :
    x = 0
    while st:
        if st[-1][0] >= v[0] : # 찾은 경우
            # x = st.pop()[1]
            x = st[-1][1]
            break
        else :
            st.pop()
    st.append(v)
    r.append(x)

print(*r)