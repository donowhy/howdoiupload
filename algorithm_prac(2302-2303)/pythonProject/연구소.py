from collections import deque

row, col = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(row)]

visited = [[0] * col for _ in range(row)]

dq = deque()

for i in range(row):
    for j in range(col):
        if a[i][j] == 2 or a[i][j] == 1:
            visited[i][j] = 1

stn = 3
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while True:
    for i in range(row):
        for j in range(col):
            if a[i][j] == 0:
                dq.append((i, j))
                visited[i][j] = 1
                x, y = dq.popleft()




from collections import deque
import copy

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0

    for i in range(n):
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0

n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
makeWall(0)
print(answer)