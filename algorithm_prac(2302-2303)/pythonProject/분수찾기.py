# 1,2,3,4,5,
#
# N = int(input())
#
# dap = 0
# for i in range(1, N):
#     dap += i
#     if dap

# N = int(input())
#
# line = 0
# end = 0
# while N > end:
#     line += 1
#     end += line
#
# diff = end - N
# if line % 2 == 0:  # 짝수 라인 일때
#     top = line - diff
#     bottom = diff + 1
# else:
#     top = diff + 1
#     bottom = line - diff
#
# print("%d/%d" % (top, bottom))

def dfs(start,idx):
    stk = []
    stk.append(lst[start][idx])
    if idx == 0:



T = int(input())

lst = [list(map(int,input().split())) for _ in range(T)]

ans = []


