# #방법 1
#
# board = [[0 for _ in range(101)] for _ in range(101)]
#
# for _ in range(4):
#     x1, y1, x2, y2 = map(int,input().split())
#     for i in range(x1, x2):
#         for j in range(y1, y2):
#             board[i][j] = 1
#
# result = 0
#
# for k in range(101):
#     for l in range(101):
#         if board[k][l] == 1:
#             result += 1
#
# print(result)
#

#방법 2

board =[]
for _ in range(4):
    lst = list(map(int, input().split()))
    for i in range(lst[0], lst[2]):
        for j in range(lst[1], lst[3]):
            board.append((i,j))

print(len(set(board)))