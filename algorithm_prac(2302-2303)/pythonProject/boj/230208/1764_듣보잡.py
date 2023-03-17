import sys

input = sys.stdin.readline

N, M = map(int,input().split())

lst = []
cnt = 0

for _ in range(N):
    lsten = input().rstrip()
    lst.append(lsten)

for _ in range(M):
    see = input().rstrip()
    lst.append(see)

lst.sort()

for i in range(len(lst)-1):
    if lst[i] == lst[i+1]:
        cnt += 1
print(cnt)

for i in range(len(lst)-1):
    if lst[i] == lst[i+1]:
        print(lst[i])


#방법 2
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = dict()
answer = []
for i in range(n):
    x = input()
    if x not in arr1:
        arr1[x] = i

for i in range(m):
    y = input()
    if y in arr1:
        answer.append(y)

answer.sort()
print(len(answer))
print(''.join(answer), end='')

#방법 3
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = []
arr2 = []
for i in range(n):
    x = input()
    arr1.append(x)
for i in range(m):
    y = input()
    arr2.append(y)

answer = list(set(arr1) & set(arr2))
answer.sort()
print(len(answer))
print(''.join(answer), end = '')