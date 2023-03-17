# from collections import deque
#
#
# def find(start):
#     for i in ans[start]:
#         if visited[i] == 0:
#             visited[i] = start
#             find(i)
#
#
# trip = int(input())
# lst = list(map(int, input().split()))
#
# arr = set(lst)
#
# ans = [[] for _ in range(trip)]
# visited = [0 for _ in range(trip)]
#
# for i in range(0, len(lst)-1):
#     if i >= 1 and lst.count(lst[i]) >= lst.count(lst[i + 1]):
#         if i < len(lst)-2 and lst[i] == lst[i+2]:
#             ans[lst[i]].append(lst[i+1])
#         elif  i < len(lst)-2 and lst[i-1] == lst[i+1]:
#             continue
#         else:
#             ans[lst[i]].append(lst[i+1])
#
#     else:
#         if i < len(lst)-2 and lst[i] == lst[i+2]:
#             ans[lst[i]].append(lst[i+1])
#         elif  i < len(lst)-2 and lst[i-1] == lst[i+1]:
#             continue
#         else:
#             ans[lst[i]].append(lst[i+1])
#
#
# visited[lst[0]] = -1
#
# print(ans)
#
# find(lst[0])
# print(len(arr))
# for x in range(len(arr)):
#     print(visited[x], end=' ')
#
# #
# import sys
# input=sys.stdin.readline
#
#
# N=int(input())
# L=list(map(int,input().split()))
#
# visit=set()
# visit.add(L[0])
# dp=[0]*(200001)
# dp[L[0]]=-1
#
# for i in range(1,N):
#     if L[i] not in visit:
#         dp[L[i]]=L[i-1]
#         visit.add(L[i])
#
# print(len(visit))
# for i in range(len(visit)):
#     print(dp[i] , end=" ")


N = int(input())
city = list(map(int,input().split()))
stack = []
dic = {}
for i in city:
    if len(stack) > 1 and stack[-2] == i:
        son = stack.pop()
        mth = stack[-1]
        dic[son] = mth
    else:
        stack.append(i)

print(len(dic) + 1)
for i in range(len(dic) + 1):
    if dic.get(i) == None:
        print(-1,end=' ')
    else:
        print(dic.get(i),end=' ')