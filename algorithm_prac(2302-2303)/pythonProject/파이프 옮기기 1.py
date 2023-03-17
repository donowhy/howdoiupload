# from collections import deque
# import sys
#
# count = 0
# N = int(input())
# home = []
# for _ in range(N):
#     home.append([int(x) for x in sys.stdin.readline().rstrip().split()])
# print(home)


# def bfs():
#     global count
#     deq = deque()
#     deq.append([0, 1, 0])  # 0 가로 1 세로 2 대각선
#
#     while deq:
#         x, y, state = deq.popleft()
#         if x == N - 1 and y == N - 1:
#             count += 1
#             continue
#
#         if state == 0:
#             if y == N - 1:
#                 continue
#
#             if 0 <= x < N and 0 <= y + 1 < N and home[x][y + 1] == 0:
#                 deq.append([x, y + 1, 0])
#
#             if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
#                 y + 1] == 0:
#                 deq.append([x + 1, y + 1, 2])
#
#         elif state == 1:
#             if x == N - 1:
#                 continue
#
#             if 0 <= x + 1 < N and 0 <= y < N and home[x + 1][y] == 0:
#                 deq.append([x + 1, y, 1])
#
#             if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
#                 y + 1] == 0:
#                 deq.append([x + 1, y + 1, 2])
#
#         elif state == 2:
#
#             if 0 <= x < N and 0 <= y + 1 < N and home[x][y + 1] == 0:
#                 deq.append([x, y + 1, 0])
#
#             if 0 <= x + 1 < N and 0 <= y < N and home[x + 1][y] == 0:
#                 deq.append([x + 1, y, 1])
#
#             if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
#                 y + 1] == 0:
#                 deq.append([x + 1, y + 1, 2])
#
#
# bfs()
# print(count)
#
#
#
#
# import sys
# count = 0
# N = int(input())
# home = []
#
# for _ in range(N):
#     home.append([int(x) for x in sys.stdin.readline().rstrip().split()])
#
# def dfs(x,y,state): # state 0: 가로, 1: 세로 , 2: 대각선
#     global count
#     if x == N - 1 and y == N - 1:
#         count += 1
#         return
#
#     if state == 0:
#         if y == N - 1: # 이동불가
#             return
#
#         if 0 <= x < N and 0 <= y + 1 < N and home[x][y + 1] == 0:
#             dfs(x, y + 1, 0)
#
#         if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
#             y + 1] == 0:
#             dfs(x + 1, y + 1, 2)
#
#     elif state == 1:
#         if x == N - 1: # 이동불가
#             return
#
#         if 0 <= x + 1 < N and 0 <= y < N and home[x + 1][y] == 0:
#             dfs(x + 1, y, 1)
#
#         if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
#             y + 1] == 0:
#             dfs(x + 1, y + 1, 2)
#
#     elif state == 2:
#         if 0 <= x < N and 0 <= y + 1 < N and home[x][y + 1] == 0:
#             dfs(x, y + 1, 0)
#
#         if 0 <= x + 1 < N and 0 <= y < N and home[x + 1][y] == 0:
#             dfs(x + 1, y, 1)
#
#         if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
#             y + 1] == 0:
#             dfs(x + 1, y + 1, 2)
#
# dfs(0,1,0)
# print(count)



import sys

home = []
N = int(input())
for _ in range(N):
    home.append([int(x) for x in sys.stdin.readline().rstrip().split()])

DP = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)] # 3차원
# 0 가로, 1 세로, 2 대각선
print(DP)

DP[0][0][1] = 1
print(DP)
for i in range(2,N):
    if home[0][i] == 0:
        DP[0][0][i] = DP[0][0][i - 1]
#print(DP)

for i in range(1,N):
    for j in range(1,N):
        if home[i][j] == 0 and home[i][j - 1] == 0 and home[i - 1][j] == 0:
            DP[2][i][j] = DP[0][i - 1][j - 1] + DP[1][i - 1][j - 1] + DP[2][i - 1][j - 1]
            # 대각선 파이프 놓기

        if home[i][j] == 0:
            DP[0][i][j] = DP[0][i][j - 1] + DP[2][i][j - 1]
            # 가로 파이프 놓기

            DP[1][i][j] = DP[1][i - 1][j] + DP[2][i - 1][j]
            # 세로 파이프 놓기
print(DP[0][N - 1][N - 1] + DP[1][N - 1][N - 1] + DP[2][N - 1][N - 1])