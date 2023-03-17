import pprint
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr = []
lst = []
for _ in range(N):
    sites = input().split()
    lst.append(sites)


for _ in range(M):
    wnt = input().split()
    arr.append(wnt)


for i in arr:
    for j in range(len(lst)):
        if (i[0]) == lst[j][0]:
            print(lst[j][1])





#방법 2
N, M = map(int, input().split())
dic = {}

for n in range(N):
    a, b = input().split()
    dic[a] = b

for m in range(M):
    a = input().strip()
    print(dic[a])