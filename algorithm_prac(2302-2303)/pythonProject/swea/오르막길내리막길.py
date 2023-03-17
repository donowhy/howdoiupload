# T = int(input())
#
# for i in range(1, T + 1):
#     N = int(input())
#     graph = []
#     stk = []
#
#     x = y = 0
#     dx = [-1, 1, 0, 0, -1, -1, 1, 1]
#     dy = [0, 0, -1, 1, -1, 1, -1, 1]
#
#     cnt = 0
#
#     for j in range(N):
#         lst = list(map(int,input().split()))
#         graph.append(lst)
#     lst = []
#     for a in range(1, N - 1):
#         for b in range(1, N - 1):
#             arr = []
#             for k in range(8):
#
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 arr.append(graph[a+nx][b+ny])
#
#             if max(arr) < graph[a][b]:
#                 lst.append(graph[a][b])
#
#
#     if len(lst) <= 1:
#         print(f'#{i} -1')
#
#     else:
#         print(f'#{i} {max(lst)- min(lst)}')
#
#
#

#우주선 착륙 2
# T = int(input())
#
# for i in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     cnt = 0
#     stk = []
#
#     dx = [1, 1, 1, 0, 0, -1, -1, -1]
#     dy = [1, -1, 0, 1, -1, 1, -1, 0]
#
#     result = 0
#     for j in range(N):
#         for k in range(M):
#             arr = 0
#             for l in range(8):
#                 # print(j, k, l)
#                 nx = j + dx[l]
#                 ny = k + dy[l]
#                 # if 0 <= nx < N and 0 <= ny < M:
#                 if nx < 0 or ny < 0 or nx >= N or ny >= M:
#                     continue
#                 if lst[nx][ny] < lst[j][k]:
#                     arr += 1
#             if arr >= 4:
#                 result += 1
#     print(f'#{i} {result}')


#로봇이 이동한 경로
T = int(input())

for i in range(1, 1 + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    stk = []  # direction
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    x = y = 0

    while 0 <= x <= N and 0 <= y <= N and visited[x][y] is False:
        visited[x][y] = True
        stk.append(lst[x][y])
        nx = x + dx[lst[x][y]]
        ny = y + dy[lst[x][y]]
        x = nx
        y = ny

    print(f'#{i}', *stk)

#방법 2
def dfs(visited, mapp, x, y):
    global direction
    if visited[x][y] == True:  # 기저조건
        return
    visited[x][y] = True  # 먼저 처음 시작하는 0,0은 방문처리

    direction.append(mapp[x][y])  # 가능 방향 저장

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    a = mapp[x][y]

    nx = x + dx[a]
    ny = y + dy[a]

    if 0 <= nx < N and 0 <= ny < N:  # 이동하세요.
        dfs(visited, mapp, nx, ny)  # 앞으로가자
        return


T = int(input())  # 구역의 개수, 테스트 케이스
N = int(input())  # 행렬의 크기

mapp = [list(map(int, input().split())) for _ in range(N)]
direction = []
visited = [[False] * N for i in range(N)]
dfs(visited, mapp, 0, 0)

print(f'#1', *direction)