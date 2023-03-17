import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int,input().split()))

hap = [0]
temp = 0

for i in num:
    temp += i
    hap.append(temp)


for _ in range(M):
    a, b = map(int, input().split())
    print(hap[b] - hap[a-1])