import sys
input = sys.stdin.readline

n = int(input())
p = [int(x) for x in input().split()]

p.sort()
s = 0
for i,x in enumerate(p):
    # s += x # ...?
    # s += x * (n - i)
    s += s+x


print(s)

'''
1 2 3 4 5
1 + (1+2) + ((1+2) + 3)'''