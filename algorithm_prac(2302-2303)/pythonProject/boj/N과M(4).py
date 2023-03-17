# n, m = map(int, input().split())
#
# s = []
#
# def dfs(start):
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(start, n + 1):
#         s.append(i)
#         print(s)
#         dfs(i)
#         s.pop()
#         print(s)
#
# dfs(1)
#

# n, m = map(int, input().split())
# lst = list(map(int, input().split()))
# lst.sort()
#
# s = []
#
# def dfs(start):
#     if len(s) == m:
#         print(' '.join(map(str,s)))
#         return
#
#     for i in range(len(lst)):
#         s.append(lst[i])
#         print(s)
#         if len(s) > 0 and s[-1] < lst[i]:
#             s.append(lst[i])
#             print(s)
#             dfs(i)
#             s.pop()
#             print(s)
#
#
#
# dfs(lst[0])
# #####(6)
# n, m = map(int, input().split())
# lst = sorted(list(map(int, input().split())))
# s = []
#
# def dfs(start):
#     if len(s) == m:
#         print(*s)
#         return
#     for i in range(start, n):
#         if lst[i] not in s:
#             s.append(lst[i])
#             dfs(i + 1)
#             s.pop()
#
# dfs(0)

## 8
# n, m = map(int, input().split())
# lst = sorted(list(map(int, input().split())))
# s = []
# lst.sort()
#
# def dfs(start):
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#
#     for i in range(start, n):
#         s.append(lst[i])
#         dfs(i)
#         s.pop()
#
#
# dfs(0)


### 9
# N, M = map(int, input().split())
# L = list(map(int, input().split()))
#
# L.sort()
# visited = [False] * N
# out = []
# all_out = []
#
# def solve(depth, N, M):
#     if depth == M:
#         tmp = ' '.join(map(str, out))
#         if tmp not in all_out:
#             all_out.append(tmp)
#         return
#     for i in range(N):
#         if not visited[i]:
#             out.append(L[i])
#             visited[i] = True
#             solve(depth+1, N, M)
#             out.pop()
#             visited[i] = False
#
# solve(0, N, M)
# for i in all_out:
#     print(i)

##-->
N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(N):
        if not visited[i] and overlap != L[i]:
            visited[i] = True
            out.append(L[i])
            overlap = L[i]
            solve(depth+1, N, M)
            visited[i] = False
            out.pop()

solve(0, N, M)

### 10
# N, M = map(int, input().split())
# L = list(map(int, input().split()))
#
# L.sort()
# visited = [False] * N
# out = []
#
# def solve(depth, idx, N, M):
#     if depth == M:
#         print(' '.join(map(str, out)))
#         return
#     overlap = 0
#     for i in range(idx, N):
#         if not visited[i] and overlap != L[i]:
#             out.append(L[i])
#             visited[i] = True
#             overlap = L[i]
#             solve(depth+1, i+1, N, M)
#             out.pop()
#             visited[i] = False
#
# solve(0, 0, N, M)


### 12
def bt(seq, cnt):
    cnt -= 1
    if cnt == -1:
        print(*seq)
        return

    for i in arr:
        if not seq or i >= seq[-1]:
            bt(seq + [i], cnt)


n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
bt([], m)