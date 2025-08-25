## 동전 0 https://www.acmicpc.net/problem/11047

'''
문제 설명
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 최소로사용해서 그 가치의 합을 K로 만들려고 한다.

입력
(1) N K : 동전 개수, 합
(2) N개줄에 동전의 가치가 오름차순으로 제공, 각 가치는 1 ≤ Ai ≤ 1,000,000

출력
k 원을 만드는데 필요한 동전 개수의 최솟값
'''

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
c = [int(input()) for _ in range(n)]

s = 0

for i in c[::-1] :
    if i > k : # 동전이 필요한 합보다 커서 사용 불가
        continue
    s += k // i # 몇번 들어갈 수 있는지
    k = k % i

    if k == 0 :
        break

print(s)

