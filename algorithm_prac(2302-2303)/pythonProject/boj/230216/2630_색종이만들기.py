# import sys
#
# N = int(sys.stdin.readline())
# paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# result = []
#
#
# def solution(x, y, N):
#     color = paper[x][y]
#     for i in range(x, x + N):
#         for j in range(y, y + N):
#             if color != paper[i][j]:
#                 solution(x, y, N // 2)
#                 solution(x, y + N // 2, N // 2)
#                 solution(x + N // 2, y, N // 2)
#                 solution(x + N // 2, y + N // 2, N // 2)
#                 return
#     if color == 0:
#         result.append(0)
#     else:
#         result.append(1)
#
#
# solution(0, 0, N)
# print(result.count(0))
# print(result.count(1))
#
#
#
#
#
#
# import sys
#
# N = int(sys.stdin.readline().rstrip())
#
# board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# result = 0
# blue = 0
#
#
# def separate(sr, sc, er, ec):
#     global result, board, N, blue
#     # print(sr, sc, er, ec, '재귀호출됨')
#
#     if sr == er and sc == ec:
#         # print('1장짜리')
#         # print(sr, sc)
#         if board[sr][sc] == 1:
#             blue += 1
#         result += 1
#         return
#
#     temp = board[sr][sc]
#     flag = True
#     for i in range(sr, er + 1):
#         for j in range(sc, ec + 1):
#             if board[i][j] != temp:
#                 flag = False
#                 break
#     if flag:
#         # print('여러 장인데 끝')
#         # print(sr, sc, er, ec)
#         if temp == 1:
#             blue += 1
#         result += 1
#         return
#     else:
#         midR = (sr + er) // 2
#         midC = (sc + ec) // 2
#
#         separate(sr, sc, midR, midC)
#         separate(sr, midC + 1, midR, ec)
#         separate(midR + 1, sc, er, midC)
#         separate(midR + 1, midC + 1, er, ec)
#
#
# def solution():
#     global N, board, result, blue
#
#     separate(0, 0, N - 1, N - 1)
#
#     print(result - blue)
#     print(blue)
#
#
# solution()
#


# T = int(input())
#
# for i in range(1, T +1):
#     stk = []
#
#     letter = input()
#
#     for j in letter:
#         # print(j)
#         try:
#             if j in ['(', '{']:
#                 stk.append(j)
#             elif j == ')':
#                 if stk[-1] == '(':
#                     stk.pop()
#             elif j == '}':
#                 if stk[-1] == '{':
#                     stk.pop()
#             print(stk)
#
#         except:
#             print(f'#{i} 0')
#             exit()
#
#     if not stk:
#         print(f'#{i} 1')
#     else:
#         print(f'#{i} 0')
#
#
# T = int(input())
#
# for i in range(1, T + 1):
#     arr = input()
#     stk = []
#
#     try:
#         for c in arr:
#             if c in ['(', '{']:
#                 stk.append(c)
#
#             elif c == ')':
#                 if stk[-1] == '(':
#                     stk.pop()
#                 else:
#                     break
#
#             elif c == '}':
#                 if stk[-1] == '{':
#                     stk.pop()
#                 else:
#                     break
#
#     except:
#         exit()
#
#     if stk:
#         print(f'#{i} 0')
#     else:
#         print(f'#{i} 1')


T = int(input())
for test_case in range(1, T + 1):
    command = input()
    stack = []

    try:
        for c in command:
            if c == '(':
                stack.append(c)
            elif c == '{':
                stack.append(c)
            elif c == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    print(f'#{test_case} 0')
                    break
            elif c == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    print(f'#{test_case} 0')
                    break
    except:
        print(f'#{test_case} 0')
    if stack:
        print(f'#{test_case} 0')
    else:

        print(f'#{test_case} 1')



#우주선 착륙
T = int(input())

for i in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    stk = []

    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [1, -1, 0, 1, -1, 1, -1, 0]

    result = 0
    for j in range(N):
        for k in range(M):
            arr = 0
            for l in range(8):
                # print(j, k, l)
                nx = j + dx[l]
                ny = k + dy[l]
                # if 0 <= nx < N and 0 <= ny < M:
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if lst[nx][ny] < lst[j][k]:
                    arr += 1
            if arr >= 4:
                result += 1
    print(f'#{i} {result}')