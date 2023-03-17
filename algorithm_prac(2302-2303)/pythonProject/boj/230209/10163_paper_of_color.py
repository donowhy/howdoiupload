# lst = [[0 for _ in range(1001)] for _ in range(1001)]
# board = []
# N = int(input())
# for j in range(N):
#     a, b, a1, b1 = map(int,input().split())
#     for i in range(b, b+ b1):
#         lst[i][a:a+a1] = [j]*a1
#
# for j in range(1, N + 1):
#     result = 0
#     for cnt in range(1001):
#         result += list[cnt].count(j)
#     print(result)
#
#
#
#
#
# # 2번째 방법
#
# from sys import stdin
# input = stdin.readline
# n = int(input())
# board = [[-1] * 1001 for _ in range(1001)]
# res = [0 for _ in range(n)]
# min_x, min_y = 1001, 1001
# max_x, max_y = 0, 0
#
# for k in range(n):
#     x, y, width, height = map(int, input().split())
#     for i in range(x, x + width):
#         for j in range(y, y + height):
#             board[i][j] = k
#     min_x, min_y = min(x, min_x), min(y, min_y)
#     max_x, max_y = max(x + width, max_x), max(y + height, max_y)
#
# for k in range(n):
#     for i in range(min_x, max_x):
#         for j in range(min_y, max_y):
#             if board[i][j] == k:
#                 res[k] += 1
#
# for i in res:
#     print(i)

#방법 3

import sys
input = sys.stdin.readline

N = int(input())
matrix = [[0]*1001 for _ in range(1001)]
for k in range(1,N+1):
    x,y,w,h = map(int, input().split())
    for i in range(x,x+w):
        for j in range(y,y+h):
            matrix[i][j] = k

cnt_color = [0] * (N+1)
for i in range(1001):
    for j in range(1001):
        if matrix[i][j]:
            cnt_color[matrix[i][j]] += 1
            print(cnt_color)

for i in range(1,N+1):
    print(cnt_color[i])