# from collections import deque
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# def bfs(start, end):
#     dq = deque
#     dq.append(start)
#     if start == end:
#         return
#     while dq:
#         x, y = dq.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or N < nx or M < ny or visited:
#                 continue
#             else:
#                 if lst[nx][ny] == 0:
#                     visited[nx][ny] = visited[x][y] +1
#                     x = nx
#                     y = ny
#                 else:
#
#
#
# N , M = map(int,input().split())
# lst = [list(map(int,input().split())) for _ in range(N)]
# visited = [[False for _ in range(M)] for _ in range(N)]
#
# print(visited)



from collections import deque

n, m = map(int, input().split())
graph = []

# 3차원 행렬을 통해 벽의 파괴를 파악함. visited[x][y][0]은 벽 파괴 가능. [x][y][1]은 불가능.
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        a, b, c = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0 :
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 곳이면
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1


print(bfs(0, 0, 0))


##########
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
ans = 0


def bfs():
    # (0, 0) 출발, 벽 안부순 상태 시작
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while q:
        r, c, wall = q.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c][wall]

        for i in range(4):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            # 맵 범위 안에 있고, 한 번도 방문하지 않았으면
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][wall] == 0:
                # 벽이 아니라면 이동하고, 이전경로 + 1 visited 배열에 저장
                if board[nr][nc] == 0:
                    q.append((nr, nc, wall))
                    visited[nr][nc][wall] = visited[r][c][wall] + 1

                # 벽 1번도 안 부쉈고, 다음 이동할 곳이 벽이라면
                if wall == 0 and board[nr][nc] == 1:
                    # 벽을 부순 상태를 1로 표현
                    q.append((nr, nc, 1))
                    # 벽 부순 상태의 visited[nr][nc][1]에 이전경로 + 1 저장
                    visited[nr][nc][1] = visited[r][c][wall] + 1

    return -1


print(bfs())