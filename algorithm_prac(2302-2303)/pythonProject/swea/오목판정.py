# from collections import deque
#
# for t in range(1, int(input()) + 1):
#     N = int(input())
#     board = [list(input()) for _ in range(N)]
#
#     locate = deque()
#     ans_col = []
#     ans_row = []
#     res = 0
#     for i in range(N):
#         ans = []
#         loc = []
#         for j in range(N):
#             if board[i][j] == 'o':
#                 locate.append([i,j])
#                 loc.append(j)
#             if board[j][i] == 'o':
#                 ans.append(j)
#
#         if len(ans) >= 5:  #세로
#             lst = []
#             for j in range(len(ans)):
#                 lst.append(ans[j:j+4])
#                 if abs(ans[-1] - ans[0]) == 4:
#                     res = 1
#         # print(loc)
#         if len(loc) >= 5:  #가로
#             lst = []
#             for j in range(len(loc)):
#                 lst.append(loc[j:j+4])
#                 if abs(loc[-1] - loc[0]) == 4:
#                     res = 1
#     i = 0
#     while locate:
#         ans_col.append(locate[i][0])
#         ans_row.append(locate[i][1])
#         locate.popleft()
#
#     while len(ans_col[i: i+4]) == 5:
#         ans_left = []
#         ans_left.append(ans_col[i:i+4])
#         if abs(ans_left[0][-1] - ans_left[0][0]) == 4:
#             res= 1
#
#         ans_left.clear()
#
#         ans_left.append(ans_row[i:i + 4])
#         if abs(ans_left[0][-1] - ans_left[0][0]) == 4:
#             res = 1
#
#         i += 1
#
#     if res == 1:
#         print(f'#{t} YES')
#     else:
#         print(f'#{t} NO')


def chk():
    for i in range(1, n + 1):  # i,j 전부 돌면서
        for j in range(1, n + 1):
            if lst[i][j] == 'o':  # 돌 발견하면 4방향에 대해 검사
                for k in range(4):
                    ci = i
                    cj = j
                    cnt = 0
                    while lst[ci][cj] == 'o':
                        ni = ci + di[k]
                        nj = cj + dj[k]
                        ci = ni
                        cj = nj
                        cnt += 1
                    if cnt >= 5:
                        return True
    return False


t = int(input())

di = (0, 1, 1, 1)  # 우, 우하, 하, 좌하
dj = (1, 1, 0, -1)

for tc in range(1, t + 1):
    n = int(input())
    lst = ['.' * (n + 2) for _ in range(n + 2)]  # padding
    print(lst)
    for i in range(n):
        lst[i + 1] = '.' + input() + '.'

    if chk():
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')