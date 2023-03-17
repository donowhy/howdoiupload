# c, r = map(int,input().split())
#
# arr = [[0]*c for _ in range(r)]
# N = int(input())
#
# for i in range(1, c+1):
#     for j in range(1,r+1):
#         if N <= (c * r):
#

#방법 1
# import sys
#
# input = sys.stdin.readline
#
# m, n = map(int, input().split())
# k = int(input())
# if k > m * n:  # 배열의 범위를 벗어남
#     print(0)
#     sys.exit()
#
# board = [[0] * m for _ in range(n)]
# board[0][0] = 1
# move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# cur_dir = 0
# x, y = (0, 0)
# for i in range(2, k + 1):
#     while True:
#         a, b = move[cur_dir]
#         dx = x + a;
#         dy = y + b
#         if n > dx >= 0 and m > dy >= 0 and board[dx][dy] == 0:
#             board[dx][dy] = i
#             x = dx;
#             y = dy  # 현재 위치 갱신
#             break
#         else:
#             cur_dir = (cur_dir + 1) % 4  # 방향전환
# print(y + 1, x + 1)


#방법 2
C,R = map(int,input().split())

my_seat = int(input())

#좌석을 줄 수 없는 경우
if my_seat > C*R :
    print(0)
    exit()

#4방향
dx = [0,1,0,-1]
dy = [-1,0,1,0]

#그리드 만들기
grid = [[0]*C for _ in range(R)]
direction = x= y = 0

#행렬 돌면서
for seat in range(1,C*R+1) :
    #내자리면 끝내기
    if seat == my_seat:
        print(y+1,x+1)
        break
    else :
        #표시하고
        print('seat', seat, 'x,y', x, y, 'direction', direction)
        grid[x][y] = seat
        #앞으로 전진
        x += dx[direction]
        y += dy[direction]

        if x<0 or y<0 or x>=R or y>=C or grid[x][y]:
            x -= dx[direction]
            y -= dy[direction]
            #범위 벗어나면 뒤로 뺐다가 방향 바꿔서 전진
            direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]