# import sys
# input = sys.stdin.readline
#
# N = int(input())
# matrix = [[0]*1001 for _ in range(1001)]
# for k in range(1,N+1):
#     x,y,w,h = map(int, input().split())
#     for i in range(x,x+w):
#         for j in range(y,y+h):
#             matrix[i][j] = k
#
# cnt_color = [0] * (N+1)
# for i in range(1001):
#     for j in range(1001):
#         if matrix[i][j]:
#             cnt_color[matrix[i][j]] += 1
#
# for i in range(1,N+1):
#     print(cnt_color[i])


'''
from sys import stdin

n = int(stdin.readline())
board = [[-1] * 1001 for _ in range(1001)]
res = [0 for _ in range(n)]
minx, miny = 1001, 1001
maxx, maxy = 0, 0

for k in range(n):
    x, y, width, height = map(int, stdin.readline().split())
    for i in range(x, x + width):
        for j in range(y, y + height):
            board[i][j] = k
    minx, miny = min(x, minx), min(y, miny)
    maxx, maxy = max(x + width, maxx), max(y + height, maxy)

for k in range(n):
    for i in range(minx, maxx):
        for j in range(miny, maxy):
            if board[i][j] == k:
                res[k] += 1

for i in res:
    print(i)
'''

s = [[0]*101 for i in range(101)] # 빈 격자판을 만든다.
n = int(input())
# 테스트 케이스 수만큼 색종이별로 테스트 케이스에 해당하는 숫자(i+1)로 채운다.
for i in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for j in range(x, x+w):
        for k in range(y, y+h):
            s[j][k] = i
for i in range(1,n+1): # 테스트 케이스 수만큼 돌며 각 색종이 면적 출력.
    cnt = 0
    for m in s:
        cnt += m.count(i)
        # print(cnt)
    print(cnt)