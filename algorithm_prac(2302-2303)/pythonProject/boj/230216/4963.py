#4963
import sys
sys.setrecursionlimit(2000)


def dfs(x, y):
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1 and visited[nx][ny] is False:
                    dfs(nx, ny)


while True:
    w, h = map(int, sys.stdin.readline().split(' '))
    if w == 0 and h == 0:
        break

    graph = [0 for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, sys.stdin.readline().split(' ')))

    visited = [[False for _ in range(w)] for _ in range(h)]

    # 8방향
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    cnt = 0
    for a in range(h):
        for b in range(w):
            if graph[a][b] == 1 and visited[a][b] is False:
                dfs(a, b)
                cnt += 1

    print(cnt)



#2667
import sys

def DFS(g, visited, i, j):
    temp = 0  # 단지 내 집 수
    def rDFS(g, i, j):
        if g[i][j] == '1' and visited[i][j] == False:
            visited[i][j] = True
            nonlocal temp
            temp += 1

            if i < N - 1 and g[i + 1][j] == '1': rDFS(g, i + 1, j)  # 아래쪽, 바깥으로 벗어나지 않도록.
            if i > 0 and g[i - 1][j] == '1': rDFS(g, i - 1, j)  # 위쪽, 바깥으로 벗어나지 않도록.
            if j < N - 1 and g[i][j + 1] == '1': rDFS(g, i, j + 1)  # 오른쪽, 바깥으로 벗어나지 않도록.
            if j > 0 and g[i][j - 1] == '1': rDFS(g, i, j - 1)  # 왼쪽, 바깥으로 벗어나지 않도록.

    rDFS(g, i, j)
    return temp

N = int(sys.stdin.readline())
g = [list(sys.stdin.readline()[:-1]) for _ in range(N)] # str으로 입력받아 0 보존.
visited = [[False for _ in range(N)] for _ in range(N)] # visited 초기화
num = 0 # 단지 수
lst = [] # 단지 내 집 수를 넣기 위한 리스트
for i in range(N):
    for j in range(N):
        if g[i][j] == '1' and visited[i][j] == False:
            lst.append(DFS(g, visited, i, j))
            num += 1

print(num)
lst.sort()
for k in range(len(lst)):
    print(lst[k])


#방법 good
import sys


def dfs(x, y):
    global cnt
    visited[x][y] = True
    if graph[x][y] == 1:
        cnt += 1
    for i in range(4):  # 네 방향
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1 and visited[nx][ny] is False:
            dfs(nx, ny)


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cntLst = []
for a in range(n):
    for b in range(n):
        if graph[a][b] == 1 and visited[a][b] is False:
            cnt = 0
            dfs(a, b)
            cntLst.append(cnt)

print(len(cntLst))
cntLst.sort()
for k in cntLst:
    print(k)