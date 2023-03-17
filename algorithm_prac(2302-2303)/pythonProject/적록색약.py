from collections import deque
import copy
def bfs(start):
    visited = [[0] * len(lst[0]) for _ in range(N)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    dq = deque()
    dq.append([0,0])
    visited[0][0] = 1
    cnt = 0

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(start[0]) and 0 <= ny < N and visited[nx][ny] == 0:
                if start[nx][ny] == 'R':
                    visited[nx][ny] = 1
                    dq.append([nx, ny])

                elif start[nx][ny] == 'G':
                    visited[nx][ny] = 2
                    dq.append([nx, ny])

                elif start[nx][ny] == 'B':
                    visited[nx][ny] = 3
                    dq.append([nx,ny])



N = int(input())
lst = [list(input()) for _ in range(N)]
visited = [[0] * len(lst[0]) for _ in range(N)]

arr = copy.deepcopy(lst)
for i in range(len(arr[0])):
    for j in range(N):
        if arr[i][j] =="G":
            arr[i][j] = 'R'

bfs(lst)
bfs(arr)





from collections import deque

def bfs(x,y):
    dq.append((x,y))
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited[x][y] = 1
    while dq:
        x, y = dq.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<=nx<N and 0<=ny<N and a[nx][ny] == a[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                dq.append((nx,ny))


N = int(input())
a = [list(input()) for _ in range(N)]
dq = deque()

# 적록색약 아닌 경우
visited = [[0] * N for _ in range(N)]
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체킹
            bfs(i,j)
            cnt1 += 1

# 적록색약인 경우
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G':
            a[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)






import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

three_cnt, two_cnt = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    #현재 색상 좌표를 방문해준다.
    visited[x][y] = True
    current_color = matrix[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if visited[nx][ny]==False:
                if matrix[nx][ny] == current_color:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if visited[i][j]==False:
            dfs(i,j)
            three_cnt += 1

#R을 G로 바꾸어준다. --> 적록색약은 같은 색으로 보기 때문에
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='R':
            matrix[i][j]='G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt,two_cnt)