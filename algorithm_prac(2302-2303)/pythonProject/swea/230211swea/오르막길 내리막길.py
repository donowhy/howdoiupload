'''
tc = int(input())

for i in range(1, tc + 1):
    N = int(input())
    number = list(map(int,input().split()))

    cnt = 0
    for j in range(1, len(number)-1):
        if number[j] != number[j-1] and number[j] != number[j+1]:
            if max(number[j], number[j-1], number[j+1]) == number[j]:
                cnt += 1
    print(f'#{i} {cnt}')
'''

'''
3
7
1 2 3 4 5 4 3
7
1 3 1 2 1 4 1
10
1 2 3 2 2 2 3 2 4 5
'''

#
# tc = int(input())
#
# for i in range(1, tc+1):
#     cnt = 0
#     board = [[0] * 101 for _ in range(101)]
#     N = int(input())
#     for j in range(N):
#         number = list(map(int,input().split()))
#         for m in range(len(number)):
#             for k in range(number[0],number[2]+1):
#                 for l in range(number[1],number[3]+1):
#                     board[k][l] = 1
#
#     for j in range(101):
#         for k in range(101):
#             if board[j][k] == 1:
#                 cnt += 1
#
#     print(f'#{i} {cnt}')

'''
tc = int(input())

for i in range(1, tc+1):
    lst = []
    arr = [[0]*101 for _ in range(101)]
    N = int(input())
    for j in range(N):
        numb = list(map(int, input().split()))
        arr[j] = numb
    for j in range(1,N-1):
        for k in range(1,N-1):
            if arr[j][k] == max(arr[j][k],arr[j-1][k],arr[j][k-1],arr[j+1][k],arr[j][k+1]) and arr[j][k] != arr[j-1][k] and arr[j][k] != arr[j][k-1] and arr[j][k] != arr[j+1][k] and arr[j][k] != arr[j][k+1]:
                lst.append(max(arr[j][k],arr[j-1][k],arr[j][k-1],arr[j+1][k],arr[j][k+1]))
    print(f'#{i} {min(lst)} {max(lst)}')

'''
'''
3
3
1 2 3
4 5 3
4 1 2
4
1 1 1 1
1 5 1 1
1 1 6 1
1 1 1 1
5
1 1 1 1 1
1 6 1 3 1
1 1 2 1 1
1 1 1 1 1
1 1 1 1 1
'''

tc = int(input())

for i in range(1, tc+1):
    board = [[0,0]]
    walk = 0
    N = int(input())
    for j in range(N):
        arr = list(map(int,input().split()))
        board.append(arr)

    for k in range(1, len(board)):
        if (board[k][0] - board[k-1][0]) >= 0 and (board[k][1] - board[k-1][1]) >= 0:
            walk += (board[k][0] - board[k-1][0]) + (board[k][1] - board[k-1][1])
        elif (board[k][0] - board[k-1][0]) < 0 and (board[k][1] - board[k-1][1]) >= 0:
            walk += (board[k][0] - board[k-1][0])*(-1) + (board[k][1] - board[k-1][1])
        elif (board[k][0] - board[k - 1][0]) >= 0 and (board[k][1] - board[k - 1][1]) < 0:
            walk += (board[k][0] - board[k - 1][0]) + (board[k][1] - board[k - 1][1])*(-1)
        else:
            walk += (board[k][0] - board[k - 1][0])*(-1) + (board[k][1] - board[k - 1][1])*(-1)
    print(f'#{i} {walk}')

#방법 2
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    where = [tuple(map(int, input().split())) for _ in range(n)] # 교수 위치 좌표
    # where.sort(key=lambda x: sum(x)) # 이건 최단 거리 때 쓸려고 넣었던 거
    # print(where)
    start = (0, 0) # 시작 지점
    total = 0
    for i in range(n): # 각 교수님에 대해서
        for j in range(2): # x, y 점 에 대해서
            a = where[i][j] - start[j] # a 는 이동 거리
            if a > 0: # 음수로 이동한 거도 양수로 바꿔주기
                total += a # 총 이동 거리에 추가
            else:
                total -= a
        start = where[i] # 시작 지점 옮겨주기
    print(f'#{tc} {total}')
