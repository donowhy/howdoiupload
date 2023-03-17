# from collections import deque
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
#
# def bfs():
#     global time
#
#     if
#
#     while ji and f:
#         x, y = ji.popleft()
#         a, b = f.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             na = a + dx[i]
#             nb = b + dy[i]
#
#
# R, C = map(int,input().split())
# lst = [list(map(int,input().split())) for _ in range(R)]
# visited_ji = [[0] * C for _ in range(R)]
# visited_f = [[0] * C for _ in range(R)]
# ji = deque()
# f = deque()
# time = 1
#
# for i in range(R):
#     for j in range(C):
#         if lst[i][j] == 'J':
#             ji.append([i,j])
#         if lst[i][j] == 'F':
#             f.append([i,j])
#         if lst[i][j] == '#':
#             visited_ji[i][j] = 1
#             visited_f[i][j] = 1
#
# bfs()
#
# print(time)

####
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(input().rstrip()))
    if 'J' in graph[i]:
        q = deque([(0, i, graph[i].index('J'))])
        print(q)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            q.append((-1, i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 'IMPOSSIBLE'

while q:
    time, x, y = q.popleft()

    # 지훈이 탈출
    if time > -1 and graph[x][y] != 'F' and (x == 0 or y == 0 or x == n - 1 or y == m - 1):
        ans = time + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#':

            # 지훈이 이동
            if time > -1 and graph[nx][ny] == '.':
                graph[nx][ny] = '_'
                q.append((time + 1, nx, ny))

            # 불 퍼뜨리기
            elif time == -1 and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                q.append((-1, nx, ny))

print(ans)


