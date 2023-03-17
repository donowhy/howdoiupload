import sys
input = sys.stdin.readline

k = int(input())
lst = list(map(int, input().split()))
tree = [[] for _ in range(k)]


def makeTree(arr, x):
    mid = len(arr) // 2
    tree[x].append(arr[mid])
    if len(arr) == 1:

        return
    makeTree(arr[:mid], x + 1)
    makeTree(arr[mid + 1:], x + 1)


makeTree(lst, 0)
for i in range(k):
    print(*tree[i])

#
# def sol(start, end, level):
#     if start == end:
#         ans[level].append(tree[start])
#         return
#     center = (start + end) // 2
#     ans[level].append(tree[center])
#     sol(start, center - 1, level + 1)
#     sol(center + 1, end, level + 1)
#
#
# Level = int(input())
# tree = list(map(int, input().split()))
# l = len(tree)
# ans = [[] for _ in range(Level)]
#
# sol(0, l - 1, 0)
# for a in ans:
#     print(*a)
