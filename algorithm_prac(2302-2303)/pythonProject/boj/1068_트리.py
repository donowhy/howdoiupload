# from collections import deque
#
# def node_del(n):
#     tree[n] = 0
#
#     node_del(2 * n - 1)
#     node_del(2 * n)
#
# N = int(input())
# tree = list(map(int,input().split()))
# tree_del = int(input())
# dq = deque()
#
# node_del(tree_del)
# print(tree)
# ###########
import sys
input = sys.stdin.readline

def dfs(num, arr):
    arr[num] = -2
    for i in range(len(arr)):
        if num == arr[i]:
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

dfs(k, arr)
count = 0
for i in range(len(arr)):
    if arr[i] != -2 and i not in arr:
        count += 1
print(count)



##########
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nodes = list(map(int, input().split()))
del_node = int(input())  # 삭제할 노드 번호
par = [[] for _ in range(N)]  # 각 노드별 자식 노드 번호
leaf = deque()  # 삭제노드의 자식노드
ans = []  # 리프노드 번호

for i in range(N):
    if nodes[i] == -1:
        continue
    else:
        par[nodes[i]].append(i)

# 리프노드 체크
for i in range(N):
    if del_node in par[i]:
        par[i].remove(del_node)
    if len(par[i]) == 0:
        ans.append(i)


# 삭제노드에 리프노드있으면 제거
if len(par[del_node]) != 0:
    for i in par[del_node]:
        leaf.append(i)
        if i in ans:
            ans.remove(i)
else:
    ans.remove(del_node)

while leaf:
    del_node = leaf.popleft()
    if par[del_node] != 0:
        for i in par[del_node]:
            leaf.append(i)
            if i in ans:
                ans.remove(i)

print(len(ans))
#
# ############
# import sys
#
# input = sys.stdin.readline
#
# def dfs(v):
#     if visited[v] != -2:
#         visited[v] = -2
#         for i in graph[v]:
#             dfs(i)
#
#
# n = int(input())
# li = list(map(int, input().split()))
#
# graph = [[] for _ in range(n)]
# for i in range(1, n):
#     graph[li[i]].append(i)
# erase = int(input())
# visited = [0] * n
#
# dfs(erase)
# # print(visited , '\n' , graph)
# cnt = 0
# for i in range(n):
#     if visited[i] != -2 and len(graph[i]) != 0:
#         cnt += 1
#
# print(cnt)