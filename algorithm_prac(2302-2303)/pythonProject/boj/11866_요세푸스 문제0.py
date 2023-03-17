# # n, k = map(int,input().split())
# #
# # lst = [i for i in range(1, n+1)]
# #
# # print(lst)
# #
# # # a = k
# # # arr = []
# # # while len(arr) != n:
# # #     arr.append(lst[a-1: a])
# # #     a += k
# # #
# # # print(arr)
#
#
# from collections import deque
#
# queue = deque()
# answer = []
#
# n, k = map(int, input().split())
#
# for i in range(1, n+1):
#     queue.append(i)
#
# while queue:
#     for i in range(k-1):
#         queue.append(queue.popleft())
#     answer.append(queue.popleft())
#
# print("<",end='')
# for i in range(len(answer)-1):
#     print(answer[i], end=', ')
# print(answer[-1], end='')
# print(">")
#
#
# # import sys
# # input = sys.stdin.readline
# # n, k = map(int,input().split())
# # circle = [x for x in range(1,n+1)]
# # removed = []
# # now = k-1
# # while circle:
# #     removed.append(circle.pop(now))
# #     if circle:
# #         now = ((now-1) + k) % len(circle)
# # print(f'<{", ".join(map(str,removed))}>')

n, k = map(int,input().split())

res = 1
dap = 1

for i in range(k):
    res *= (n - i)
    dap *= i + 1
ans = res // dap
print(ans)