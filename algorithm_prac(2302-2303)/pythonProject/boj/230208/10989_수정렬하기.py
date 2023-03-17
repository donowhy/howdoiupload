import sys
input = sys.stdin.readline

N = int(input().strip())

lst = []

for i in range(N):
    M = int(input().strip())
    lst.append(M)


for i in range(N-1):
    mindex = i
    for j in range(i+1, N):
        if lst[j] < lst[mindex]:
            mindex = j

    lst[i], lst[mindex] = lst[mindex], lst[i]

for i in range(N):
    print(lst[i])

#정답
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)