# import sys
# from collections import deque
#
# m, n, h = map(int, input().split())  # mn크기, h상자수
# graph = []
# queue = deque([])
#
# for i in range(h):
#     tmp = []
#     for j in range(n):
#         tmp.append(list(map(int, sys.stdin.readline().split())))
#         for k in range(m):
#             if tmp[j][k] == 1:
#                 queue.append([i, j, k])
#     graph.append(tmp)
#
# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, 1, -1, 0, 0]
# dz = [0, 0, 0, 0, 1, -1]
# while (queue):
#     x, y, z = queue.popleft()
#
#     for i in range(6):
#         a = x + dx[i]
#         b = y + dy[i]
#         c = z + dz[i]
#         if 0 <= a < h and 0 <= b < n and 0 <= c < m and graph[a][b][c] == 0:
#             queue.append([a, b, c])
#             graph[a][b][c] = graph[x][y][z] + 1
#
# day = 0
# for i in graph:
#     for j in i:
#         for k in j:
#             if k == 0:
#                 print(-1)
#                 exit(0)
#         day = max(day, max(j))
# print(day - 1)
#
#
# #방법 2
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# m, n, h = map(int, input().split())
#
# dx = [-1, 1, 0, 0, 0, 0]
# dy = [0, 0, -1, 1, 0, 0]
# dz = [0, 0, 0, 0, -1, 1]
#
# data = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# queue = deque()
#
#
# # 3차원 bfs문제
# def bfs():
#     while queue:
#         # 높이, x,y 순서
#         z, x, y = queue.popleft()
#         for i in range(6):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             nz = z + dz[i]
#             if -1 < nx < n and -1 < ny < m and -1 < nz < h:
#                 # 높이, x,y 순서
#                 if data[nz][nx][ny] == 0:
#                     data[nz][nx][ny] = data[z][x][y] + 1
#                     queue.append((nz, nx, ny))
#
#
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             # 높이, x,y 순서
#             if data[i][j][k] == 1:
#                 # 높이, x,y 순서
#                 queue.append((i, j, k))
# bfs()
# flag = 0
# result = -2
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             # 높이, x,y 순서
#             if data[i][j][k] == 0:
#                 flag = 1
#                 # 높이, x,y 순서
#             result = max(result, data[i][j][k])
# if flag == 1:
#     print(-1)
# elif result == -1:
#     print(0)
# else:
#     print(result - 1)







