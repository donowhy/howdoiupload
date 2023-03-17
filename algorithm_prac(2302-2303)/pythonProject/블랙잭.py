# N, M = map(int,input().split())
# lst = list(map(int,input().split()))
# max = 0
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             if lst[i] + lst[j] + lst[k] <= M and i != j and i != k and j != k:
#                 if max <= lst[i] + lst[j] + lst[k]:
#                     max = lst[i] + lst[j] + lst[k]
#
# print(max)


#
# import sys
# input = sys.stdin.readline
# T  = int(input())
# square = 0
# for i in range(1, T+1):
#     check = []
#     for j in range(2, i//2+1):
#         if i % j == 0:
#             if j in check:
#                 break
#             else:
#                 square += 1
#                 check.append(i//j)
#     square += 1
# print(square)
#

# T = int(input())
# lst = [[0] * 101 for _ in range(101)]
# for z in range(1, T + 1):
#     N, M = map(int, input().split())
#     for i in range(N, N + 10):
#         for j in range(M, M + 10):
#             lst[i][j] = 1
# cnt = 0
# for i in range(101):
#     for j in range(100):
#         if lst[i][j] + lst[i][j+1] == 1:
#             cnt += 1
#
#         if lst[j][i] + lst[j+1][i] == 1:
#             cnt += 1
#
# print(cnt)



# #아기상어
# # 아기 상어의 크기는 초기 2 만약 물고기 2마리를 먹으면 크기가 3이된다.
# # 크기가 같거나 작은 물고기는 지나갈 수 있지만 더 큰 물고기는 지나가지 못한다.
# # 먹을 수 있는 물고기가 많다면 가장 가까운 물고기를 먹으러 간다.
# # 거리가 가까운 물고기가 많다면, 가장 위에 물고기, 여러마리면 왼쪽
#
# def find():
#
#
#
# T = int(input())
# lst = [list(map(int,input().split())) for _ in range(T)]
# arr = []
# for i in range(T):
#     for j in range(T):
#         arr.append([i,j])

from collections import deque
#
# def game():
#     x, y = loc.pop()
#     while command:
#         fur = command.popleft()
#         if fur == 'U':
#             if lst[x - 1][y] != '#' and (lst[x - 1][y] != 'b' and lst[x - 2][y] != 'b'):
#                 x = x - 1
#             elif lst[x - 1][y] != '#' and lst[x-2][y] != '#' and lst[x - 1][y] == 'b' and lst[x-2][y] != 'b':
#                 x = x - 1
#                 lst[x+1][y] = '.'
#
#                 if lst[x - 1][y] == '+':
#                     lst[x-1][y] == 'B'
#                 else:
#                     lst[x-1][y] = 'b'
#
#                 if lst[x][y] == '+':
#                     lst[x][y] == 'W'
#                 else:
#                     lst[x][y] = 'w'
#
#         if fur == 'L':
#             if lst[x][y-1] != '#' and (lst[x][y-1] != 'b' and lst[x][y-2] != 'b'):
#                 x = x - 1
#             elif lst[x][y-1] != '#' and lst[x][y-2] != '#' and lst[x][y-1] == 'b' and lst[x][y-2] != 'b':
#                 y = y - 1
#                 lst[x][y+1] = '.'
#
#                 if lst[x][y-1] == '+':
#                     lst[x][y-1] == 'B'
#                 else:
#                     lst[x][y-1] = 'b'
#
#                 if lst[x][y] == '+':
#                     lst[x][y] == 'W'
#                 else:
#                     lst[x][y] = 'w'
#
#         if fur == 'R':
#             if lst[x][y+1] != '#' and (lst[x][y+1] != 'b' and lst[x][y+2] != 'b'):
#                 x = x - 1
#             elif lst[x][y+1] != '#' and lst[x][y+2] and lst[x][y+1] == 'b' and lst[x][y+2] != 'b':
#                 y = y + 1
#                 lst[x][y-1] = '.'
#
#                 if lst[x][y+1] == '+':
#                     lst[x][y+1] == 'B'
#                 else:
#                     lst[x][y+1] = 'b'
#
#                 if lst[x][y] == '+':
#                     lst[x][y] == 'W'
#                 else:
#                     lst[x][y] = 'w'
#
#         if fur == 'D':
#             if lst[x + 1][y] != '#' and (lst[x + 1][y] != 'b' and lst[x + 2][y] != 'b'):
#                 x = x + 1
#             elif lst[x + 1][y] != '#' and lst[x + 2][y] and lst[x + 1][y] == 'b' and lst[x + 2][y] != 'b':
#                 x = x + 1
#                 lst[x - 1][y] = '.'
#
#                 if lst[x + 1][y] == '+':
#                     lst[x + 1][y] == 'B'
#                 else:
#                     lst[x + 1][y] = 'b'
#
#                 if lst[x][y] == '+':
#                     lst[x][y] == 'W'
#                 else:
#                     lst[x][y] = 'w'

while True:
    loc = []
    N, M = map(int,input().split())
    if N == M == 0:
        break
    lst = [list(input()) for _ in range(N)]
    command = deque(list(input()))
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'w':
                loc.append([i,j])
    x, y = loc.pop()
    while command:
        fur = command.popleft()
        print(fur)
        if fur == 'U':
            if lst[x - 1][y] != '#' and (lst[x - 1][y] != 'b' and lst[x - 2][y] != 'b'):
                lst[x][y] = '.'
                x = x - 1
                lst[x][y] = 'w'
            elif lst[x - 1][y] != '#' and (lst[x - 1][y] != 'b' and lst[x - 2][y] == 'b'):
                lst[x][y] = '.'
                x = x - 1
                lst[x][y] = 'w'
            elif lst[x - 1][y] != '#' and lst[x - 2][y] != '#' and lst[x - 1][y] == 'b' and lst[x - 2][y] != 'b':
                lst[x][y] = '.'
                x = x - 1
                if lst[x - 1][y] == '+':
                    lst[x - 1][y] = 'B'
                else:
                    lst[x - 1][y] = 'b'

                if lst[x][y] == '+':
                    lst[x][y] = 'W'
                else:
                    lst[x][y] = 'w'

        if fur == 'L':
            if lst[x][y - 1] != '#' and (lst[x][y - 1] != 'b' and lst[x][y - 2] != 'b'):
                lst[x][y] = '.'
                y = y - 1
                lst[x][y] = 'w'
            elif lst[x][y - 1] != '#' and (lst[x][y - 1] != 'b' and lst[x][y - 2] == 'b'):
                lst[x][y] = '.'
                y = y - 1
                lst[x][y] = 'w'
            elif lst[x][y - 1] != '#' and lst[x][y - 2] != '#' and lst[x][y - 1] == 'b' and lst[x][y - 2] != 'b':
                lst[x][y] = '.'
                y = y - 1
                if lst[x][y - 1] == '+':
                    lst[x][y - 1] = 'B'
                else:
                    lst[x][y - 1] = 'b'

                if lst[x][y] == '+':
                    lst[x][y] = 'W'
                else:
                    lst[x][y] = 'w'

        if fur == 'R':
            if lst[x][y + 1] != '#' and (lst[x][y + 1] != 'b' and lst[x][y + 2] != 'b'):
                lst[x][y] = '.'
                y = y + 1
                lst[x][y] = 'w'
            elif lst[x][y + 1] != '#' and (lst[x][y + 1] != 'b' and lst[x][y + 2] == 'b'):
                lst[x][y] = '.'
                y = y + 1
                lst[x][y] = 'w'
            elif lst[x][y + 1] != '#' and lst[x][y + 2] != '#' and lst[x][y + 1] == 'b' and lst[x][y + 2] != 'b':
                lst[x][y] = '.'
                y = y + 1
                if lst[x][y + 1] == '+':
                    lst[x][y + 1] = 'B'
                else:
                    lst[x][y + 1] = 'b'

                if lst[x][y] == '+':
                    lst[x][y] = 'W'
                else:
                    lst[x][y] = 'w'

        if fur == 'D':
            if lst[x + 1][y] != '#' and (lst[x + 1][y] != 'b' and lst[x + 2][y] != 'b'):
                lst[x][y] = '.'
                x = x + 1
                lst[x][y] = 'w'
            elif lst[x + 1][y] != '#' and (lst[x + 1][y] != 'b' and lst[x + 2][y] == 'b'):
                lst[x][y] = '.'
                x = x + 1
                lst[x][y] = 'w'
            elif lst[x + 1][y] != '#' and lst[x + 2][y] != '#' and lst[x + 1][y] == 'b' and lst[x + 2][y] != 'b':
                x = x + 1
                lst[x - 1][y] = '.'

                if lst[x + 1][y] == '+':
                    lst[x + 1][y] = 'B'
                else:
                    lst[x + 1][y] = 'b'

                if lst[x][y] == '+':
                    lst[x][y] = 'W'
                else:
                    lst[x][y] = 'w'

    print(lst)