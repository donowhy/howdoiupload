# a, b = map(int,input().split())
#
# lst = list(map(int,input().split()))
# arr = [0]
# hp = 0
# for i in lst:
#     hp += i
#     arr.append(hp)
#
# res = []
# for i in range(b,len(arr)):
#     res.append(arr[i] - arr[i-b])
#
# mx = max(res)
#
# ct = res.count(mx)
# if mx:
#     print(mx,'\n',ct, sep='')
# else:
#     print('SAD')

from itertools import permutations

n = int(input())
lst = list(input().split())

arr = []

for i in range(0,10):
    arr.append(i)

combi = list(permutations(arr,n+1))

ans = []

for i in combi:
    if ans:
        break
    for j in range(n):

        if j == n-1:
            if lst[j] == '<':
                if i[j] < i[j + 1]:
                    ans.append(i)


            elif lst[j] == '>':
                if i[j] > i[j + 1]:
                    ans.append(i)
        else:
            if lst[j] == '<':
                if i[j] < i[j+1]:
                    continue
                else:
                    break

            elif lst[j] == '>':
                if i[j] > i[j+1]:
                    continue
                else:
                    break
stk = []
for i in range(len(combi)-1,0,-1):
    if stk:
        mx = list(stk[0])
        mn = list(ans[0])

        print(*mx, "\n", *mn, sep='')
        exit()
    for j in range(n):
        if j == n-1:
            if lst[j] == '<':
                if combi[i][j] < combi[i][j + 1]:
                    stk.append(combi[i])


            elif lst[j] == '>':
                if combi[i][j] > combi[i][j + 1]:
                    stk.append(combi[i])
        else:
            if lst[j] == '<':
                if combi[i][j] < combi[i][j+1]:
                    continue
                else:
                    break

            elif lst[j] == '>':
                if combi[i][j] > combi[i][j+1]:
                    continue
                else:
                    break



# n = int(input())
# ine_sing = list(map(str,input().split()))
#
# visited = [0]*10
# max_ans =""
# min_ans =""
#
# def check(i,j,k):
#     if k=='<':
#         return i<j
#     else:
#         return i>j
#
# def solve(idx,s):
#     global max_ans,min_ans
#
#     if(idx==n+1):
#         if(len(min_ans)==0):
#             min_ans = s
#         else:
#             max_ans = s
#         return
#     for i in range(10):
#         if(visited[i]==0):
#             if(idx==0 or check(s[-1],str(i),ine_sing[idx-1])):
#                 visited[i]=True
#                 solve(idx+1,s+str(i))
#                 visited[i]=False
#
#
# solve(0,"")
# print(max_ans)
# print(min_ans)