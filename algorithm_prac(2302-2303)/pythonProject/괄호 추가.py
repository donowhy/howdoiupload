# import sys
#
# n = int(input())
# s = input()
# result = -1 * sys.maxsize
#
# def myOperator(num1, oper, num2):
#     if oper == '+':
#         return num1 + num2
#     if oper == '-':
#         return num1 - num2
#     if oper == '*':
#         return num1 * num2
#
# def dfs(index, value):
#     global result
#
#     if index == n - 1:
#         result = max(result, value);
#         return
#
#     if index + 2 < n:
#         dfs(index + 2, myOperator(value, s[index + 1], int(s[index + 2])))
#
#     if index + 4 < n:
#         dfs(index + 4, myOperator(value, s[index + 1], myOperator(int(s[index + 2]), s[index + 3], int(s[index + 4]))))
#
# dfs(0, int(s[0]))
# print(result)


# switch = ['N'] + list(input())
# cnt = 0
#
# for i in range(1, len(switch)):
#     if switch == ['N'] * (len(switch)):
#         break
#     if switch[i] == 'N':
#         continue
#     for j in range(i, len(switch)):
#         if j % i == 0:
#             if switch[j] == 'Y':
#                 switch[j] = 'N'
#             else:
#                 switch[j] = 'Y'
#     cnt += 1
# print(cnt)

# import sys
#
# input = sys.stdin.readline
#
# info = {
#     "R": (0, 1),
#     "L": (0, -1),
#     "B": (1, 0),
#     "T": (-1, 0),
#     "RT": (-1, 1),
#     "LT": (-1, -1),
#     "RB": (1, 1),
#     "LB": (1, -1)
# }
#
# king, stone, n = input().split()
# kr, kc = 8 - int(king[1]), ord(king[0]) - ord("A")
# sr, sc = 8 - int(stone[1]), ord(stone[0]) - ord("A")
# for _ in range(int(n)):
#     cmd = input().strip()
#     dr, dc = info[cmd]
#     if not (0 <= kr + dr < 8 and 0 <= kc + dc < 8):
#         continue
#     kr += dr
#     kc += dc
#     if (kr, kc) == (sr, sc):
#         if not (0 <= sr + dr < 8 and 0 <= sc + dc < 8):
#             kr -= dr
#             kc -= dc
#             continue
#         sr += dr
#         sc += dc
#
# print(chr(ord("A") + kc) + str(8 - kr))
# print(chr(ord("A") + sc) + str(8 - sr))


#
# king, stone, N = input().split()
# k = list(map(int, [ord(king[0]) - 64, king[1]]))
# s = list(map(int, [ord(stone[0]) - 64, stone[1]]))
#
# move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1],
#         'LB': [-1, -1]}
#
# for _ in range(int(N)):
#     m = input()
#
#     nx = k[0] + move[m][0]
#     ny = k[1] + move[m][1]
#
#     if 0 < nx <= 8 and 0 < ny <= 8:
#         if nx == s[0] and ny == s[1]:
#             sx = s[0] + move[m][0]
#             sy = s[1] + move[m][1]
#
#             if 0 < sx <= 8 and 0 < sy <= 8:
#                 k = [nx, ny]
#                 s = [sx, sy]
#         else:
#             k = [nx, ny]
# print(f'{chr(k[0] + 64)}{k[1]}')
# print(f'{chr(s[0] + 64)}{s[1]}')

# tc = int(input())
# for t in range(tc):
#     N, M = map(int,input().split())
#     brd = [list(map(int,input().split())) for _ in range(N)]
#     ans = []
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             hap = []
#             for m in range(M):
#                 for k in range(M):
#                     hap.append(brd[i+m][j+k])
#             # print(hap)
#             ans.append(sum(hap))
#     print(f'#{t+1} {max(ans)}')






# 파리퇴치 3
#
# def sipja():
#     global N, M
#
#     for m in range(M - 1):
#         dx = [1 + m, -1 - m, 0, 0]
#         dy = [0, 0, 1 + m, -1 - m]
#         for x in range(N):
#             for y in range(N):
#                 ans_imsi = []
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if nx > N - 1 or nx < 0 or ny > N - 1 or ny < 0:
#                         continue
#                     else:
#                         ans_imsi.append(lst[nx][ny])
#                 ans[x][y] += sum(ans_imsi)
#
#     for x in range(N):
#         for y in range(N):
#             ans[x][y] += lst[x][y]
#
#     mx = 0
#     for x in range(N):
#         for y in range(N):
#             if mx < ans[x][y]:
#                 mx = ans[x][y]
#     return mx
#
#
# def cross():
#     global N, M
#
#     for m in range(M - 1):
#         dx = [1 + m, -1 - m, -1 - m, 1 + m]
#         dy = [1 + m, -1 - m, 1 + m, -1 - m]
#         for x in range(N):
#             for y in range(N):
#                 ans_imsi = []
#                 for k in range(4):
#                     nx = x + dx[k]
#                     ny = y + dy[k]
#                     if nx > N - 1 or nx < 0 or ny > N - 1 or ny < 0:
#                         continue
#                     else:
#
#                         ans_imsi.append(lst[nx][ny])
#                 res[x][y] += sum(ans_imsi)
#
#     for x in range(N):
#         for y in range(N):
#             res[x][y] += lst[x][y]
#     mx = 0
#     for x in range(N):
#         for y in range(N):
#             if mx < res[x][y]:
#                 mx = res[x][y]
#     return mx
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     ans = [[0] * N for _ in range(N)]
#     res = [[0] * N for _ in range(N)]
#
#     print(f'#{tc} {max(sipja(), cross())}')
#
#
#
#
#
#
#
#
#
#
# def cross(x, y):
#     dx = [1, 0, -1, 0]
#     dy = [0, -1, 0, 1]
#
#     sum = mapp[x][y]
#     for k in range(4):
#         for l in range(1, m):
#             nx = x + dx[k] * l
#             ny = y + dy[k] * l
#             if 0 <= nx < n and 0 <= ny < n:
#                 sum += mapp[nx][ny]
#     return sum
#
#
# def plus(x, y):
#     dx = [1, 1, -1, -1]
#     dy = [1, -1, 1, -1]
#
#     sum = mapp[x][y]
#     for k in range(4):
#         for l in range(1, m):
#             nx = x + dx[k] * l
#             ny = y + dy[k] * l
#             if 0 <= nx < n and 0 <= ny < n:
#                 sum += mapp[nx][ny]
#     return sum
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     mapp = [list(map(int, input().split())) for _ in range(n)]
#     lst = []
#     for i in range(n):
#         for j in range(n):
#             lst.append(cross(i, j))
#             lst.append(plus(i, j))
#     print(f'#{tc} {max(lst)}')


#정수 삼각형

# def mx(triangle):
#     for i in range(1, len(triangle)):
#         for j in range(i + 1):
#             if j == 0:
#                 triangle[i][j] += triangle[i - 1][j]
#             elif j == i:
#                 triangle[i][j] += triangle[i - 1][-1]
#             else:
#                 triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
#
#     return max(triangle[-1])
#
# t = int(input())
# lst = [list(map(int,input().split())) for _ in range(t)]
# print(mx(lst))


#창고 다각형

# t = int(input())
#
# brd = [[0] * 1001 for _ in range(1001)]
# height = []
# for tc in range(t):
#     l, h = map(int,input().split())
#     height.append([l,h])
#
# height.sort()
# temp = []
# for i in range(len(height)):
#     temp.append(height[i][1])
#
# col = height[-1][0] - height[0][0]
# row = max(temp)
#
# width = (col+1) * row
#
# arr = [[height[0][0],height[0][1]]]
# for i in range(temp.index(max(temp))):
#     if arr[0][1] < height[i+1][1]: # 4, 6
#         x, y = arr.pop()
#         width = width - (height[i + 1][0] - x) * (max(temp) - y)
#         arr.append([height[i+1][0],height[i+1][1]])
#
#     else:
#         continue
#
# arr.clear()
# arr.append([height[-1][0],height[-1][1]])
#
# for i in range(len(height)-1, temp.index(max(temp)), -1):
#     if arr[0][1] < height[i-1][1]: # 8, 6
#         x, y = arr.pop()
#         width = width - abs((height[i - 1][0] - (x)) * (max(temp) - y))
#         arr.append([height[i-1][0],height[i-1][1]])
#
#     else:
#         continue
#
# print(width)
#
#
#
#
# n = int(input())
# mxh = mxl = 0
# lst = []
#
# for _ in range(n):
#     l, h = map(int, input().split())
#     lst.append([l, h])
#     if mxh < h:
#         mxh = h
#         mx_idx = l
#     if mxl < l:
#         mxl = l
#
# empty_lst = [0] * (mxl + 1)
# for l, h in lst:
#     empty_lst[l] = h  # [0, 0, 4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8]
#
# now_h = 0
# total = 0
# for i in range(mx_idx + 1):
#     if empty_lst[i] > now_h:
#         now_h = empty_lst[i]
#     total += now_h
#
# now_h = 0
# for j in range(mxl, mx_idx, -1):
#     if now_h < empty_lst[j]:
#         now_h = empty_lst[j]
#     total += now_h
# print(total)
#
# '''
# 5
# 13 4
# 6 5
# 4 3
# 11 3
# 9 5
# '''


#미로 2
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(r, c):
    queue = []
    queue.append([r, c])

    while queue:
        row, column = queue.pop(0)

        if maze[row][column] != 1:
            maze[row][column] = 1

            for i in range(4):
                nr = row + dr[i]
                nc = column + dc[i]

                if 0 <= nr < 100 and 0 <= nc < 100:
                    if maze[nr][nc] == 0:
                        queue.append([nr, nc])
                    elif maze[nr][nc] == 3:
                        return 1
    return 0


for _ in range(10):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(100)]
    print(f'#{N} {bfs(1, 1)}')