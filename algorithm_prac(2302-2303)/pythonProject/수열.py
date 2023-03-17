# import sys
# input = sys.stdin.readline
#
# a, b = map(int,input().split())
# lst = list(map(int,input().split()))
# arr = []
# for i in range(len(lst)- b + 1):
#     arr.append(sum(lst[i:i+b]))
# print(arr)
# print(max(arr))


# import sys
#
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
#
# result = []
# result.append(sum(a[:k]))
# print(result)
#
# for i in range(n - k):
#     result.append(result[i] - a[i] + a[k + i])
#     print(result, a[i], a[k+i])
# print(max(result))

#
#
# from collections import deque
# import sys
# input = sys.stdin.readline
#
# n= int(input())
# a = list(map(int, input().split()))
# fst = a.pop(0)
# print(fst)
# dq = deque()
# dq.append(fst)
# ans = deque()
# ans.append(fst)
# i = 0
# while a:
#     temp = a.pop(i)
#     if dq[-1] <= temp:
#         dq.append(temp)
#     else:
#         jung = dq[-1]
#         print(jung)
#         dq.clear()
#         dq.append(jung)
#     if ans[-1] >= temp:
#         ans.append(temp)
#     else:
#         dap = ans[-1]
#         ans.clear
#         print(ans, 'ans')
#         ans.append(dap)
#
#
#
#     # else:
#     #     dq.append(temp)
#
#
# N = int(input())
# li = list(map(int, input().split()))
# dp1, dp2 = [1]*N, [1]*N
# for i in range(1, N):
#     if li[i] <= li[i-1]:
#         dp1[i] = max(dp1[i], dp1[i-1]+1)
#     if li[i] >= li[i-1]:
#         dp2[i] = max(dp2[i], dp2[i-1]+1)
# print(max(max(dp1), max(dp2)))
