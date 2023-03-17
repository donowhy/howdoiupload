# import sys
# import heapq
#
# for T in range(int(sys.stdin.readline())):
#     k = int(sys.stdin.readline())
#     visited = [False] * k
#     maxH, minH = [], []
#     for i in range(k):
#         operation, n = sys.stdin.readline().split()
#         n = int(n)
#
#         if operation == 'I':
#             heapq.heappush(minH, (n, i))
#             heapq.heappush(maxH, (-n, i))
#             visited[i] = True
#         elif n == 1:
#             while maxH and not visited[maxH[0][1]]:
#                 heapq.heappop(maxH)
#             if maxH:
#                 visited[maxH[0][1]] = False
#                 heapq.heappop(maxH)
#         else:
#             while minH and not visited[minH[0][1]]:
#                 heapq.heappop(minH)
#             if minH:
#                 visited[minH[0][1]] = False
#                 heapq.heappop(minH)
#     while minH and not visited[minH[0][1]]:
#         heapq.heappop(minH)
#     while maxH and not visited[maxH[0][1]]:
#         heapq.heappop(maxH)
#     print(-maxH[0][0], minH[0][0]) if maxH and minH else print("EMPTY")
#
#
#
#
#
# from collections import deque
#
# tc = int(input())
#
# for t in range(tc):
#     num = int(input())
#     res = 0
#     dq = deque()
#     for i in range(num):
#
#         lst = list(input().split())
#         a = int(lst[1])
#
#         if lst[0] == 'I':
#             if len(dq) == 0:
#                 dq.append(a)
#             else:
#                 if a < dq[0]:
#                     dq.appendleft(a)
#                 elif dq[-1] < a:
#                     dq.append(a)
#
#         elif lst[0] == 'D':
#             if len(dq) == 0:
#                 res = 1
#
#             else:
#                 if a == 1:
#                     dq.pop()
#                 elif a == -1:
#                     dq.popleft()
#         if len(dq) == 0:
#             continue
#
#     if res:
#         print('EMPTY')
#     else:
#         print(dq[-1], dq[0])
#
#
# '''
# 1
# 9
# I 36
# I 37
# I 38
# D 1
# D 1
# I 39
# I 40
# D -1
# D -1
# '''


T = int(input())

lst = list(map(int,input().split()))
wnt = int(input())

lst.sort()
start = 0
end = len(lst) - 1
cnt = 0

while True:
    if lst[start] + lst[end] > wnt:
        end -= 1

    elif lst[start] + lst[end] < wnt:
        start += 1

    elif lst[start] + lst[end] == wnt:
        cnt += 1
        start += 1

    if start >= end:
        break
print(cnt)
