import sys
input = sys.stdin.readline

n = int(input())
arr = [int(x) for x in  input().split()]

m = int(input())
t = [int(x) for x in  input().split()]
result = [0] * m

arr.sort()
for i,x in enumerate(t):
    l = 0
    r = n - 1
    y = 0
    while l <= r :
        mid = arr[(l+r)//2]

        if x > mid :
            l = (l+r)//2 + 1

        elif x < mid :
            r = (l+r)//2 - 1

        else :
            y = 1
            break
    result[i] = y

print("\n".join(map(str, result)))