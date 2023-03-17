#배열 돌리기 1
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 하우상좌


def rotate():
    carr = [[] for _ in range(N)]

    for i in range(N):#배열 복사
        carr[i]=arr[i][:]

    sr = 0; sc = 0; er = N - 1; ec = M - 1
    for depth in range(min(M, N)//2):
        r = sr
        c = sc
        for d in move:
            while True:
                nr = r + d[0]
                nc = c + d[1]
                if sr <= nr <= er and sc <= nc <= ec:
                    arr[nr][nc] = carr[r][c]
                    r = nr
                    c = nc
                else:
                    break
        sr+=1; sc+=1; er-=1; ec-=1


for r in range(R % ((N-1) * (M))):  # 전체 회전 횟수
    rotate()

for i in range(N):
    print(*arr[i])




from collections import deque

N, M, R = map(int, input().split())  # N*M 배열을 반시계로 R번 돌림
arr = [list(map(int, input().split())) for _ in range(N)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def rotate():
    q = deque()
    for depth in range(min(N, M) // 2):
        r = c = depth

        for dr, dc in move:  # 큐에 담아놓고
            while True:
                nr = r + dr
                nc = c + dc
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    q.append(arr[r][c])
                    r = nr
                    c = nc
                else:
                    break

        # 돌린다
        for _ in range(R % ((N - depth * 2) * 2 + (M - depth * 2) * 2 - 4)):
            q.appendleft(q.pop())

        for dr, dc in move: #큐에서 돌린 값을 넣는다
            while True:
                nr = r + dr
                nc = c + dc
                if depth <= nr < N - depth and depth <= nc < M - depth:
                    arr[r][c]=q.popleft()
                    r = nr
                    c = nc
                else:
                    break

# 큐에서 값을 빼 저장한다
rotate()

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()






import sys

N, M, R = map(int, sys.stdin.readline().split())
array = []
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

# 한바퀴 회전
def rotate(i, j, n, m):
    top = array[i][j]
    left = array[n - 1][j]
    bottom = array[n - 1][m - 1]
    right = array[i][m - 1]
    for x in range(n-1, i, -1):                 # left
        array[x][j] = array[x-1][j]
    for x in range(i, n-1):                     # right
        array[x][m - 1] = array[x+1][m - 1]
    for y in range(j, m - 1):                   # top
        array[i][y] = array[i][y + 1]
    for y in range(m-1, j, -1):                 # bottom
        array[n - 1][y] = array[n - 1][y-1]
    array[i+1][j] = top
    array[n-1][j+1] = left
    array[n-2][m-1] = bottom
    array[i][m-2] = right


deep = min(N, M) // 2  					# 몇번이나 안쪽으로 들어가는지?
cycle = (N - 1) * 2 + (M - 1) * 2  		# 4x4 경우, 둘레 = 12 -> 12번 돌면 원상복구

for i in range(deep): 					# 겉 - 안쪽 - 안쪽 ... 순으로
    for _ in range(R % cycle):			# 회전 횟수 압축
        rotate(i, i, N - i, M - i)
    cycle -= 8  						# 겉과 안쪽의 둘레 차 (규칙적으로 -8) = 8칸 차이

for x in array:
    print(*x, sep=' ')