import sys

input = sys.stdin.readline

N, M = map(int, input().split())

relationship = [[] for _ in range(N)]
visited = [False] * N
result = False

for _ in range(M):
    a, b = map(int, input().split())
    relationship[a].append(b)
    relationship[b].append(a)


def dfs(depth, x):
    global result
    if depth == 4:
        result = True
        return

    for i in relationship[x]:
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False


for i in range(N):
    visited[i] = True
    dfs(0, i)
    visited[i] = False
    if result:
        break

if result:
    print(1)
else:
    print(0)

n = int(input())  # 계단 개수
s = [int(input()) for _ in range(n)]  # 계단 리스트
dp = [0] * (n)  # dp 리스트
if len(s) <= 2:  # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(s))
else:  # 계단이 3개 이상일 때
    dp[0] = s[0]  # 첫째 계단 수동 계산
    dp[1] = s[0] + s[1]  # 둘째 계단까지 수동 계산
    for i in range(2, n):  # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
    print(dp[-1])
