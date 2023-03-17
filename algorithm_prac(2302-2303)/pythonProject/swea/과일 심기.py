# for t in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(N)]
#     cnt = cnt2 = hap = hap2 = 0
#     dq = []
#     arr = []
#     arr2 = []
#     num = M
#
#     while num > 0:
#         if num % 2:
#             for i in range(N):
#                 if lst[i][num - 1]:
#                     hap += lst[i][num - 1]
#                     cnt += 1
#                     arr.append(lst[i][num - 1])
#
#         else:
#             for i in range(N):
#                 cnt += 1
#                 cnt2 += 1
#                 hap += lst[i][num - 1]
#                 hap2 += lst[i][num - 2]
#                 arr.append(lst[i][num - 1])
#                 arr2.append(lst[i][num - 2])
#
#         num -= 2
#
#     for j in range(M,1,-2):
#         for i in range(N):
#             if max(hap, hap2) == hap:
#                 if max(arr) == lst[i][j - 1]:
#                     dq.append(j-1)
#             if max(hap, hap2) == hap2:
#                 if max(arr) == lst[i][j - 2]:
#                     dq.append(j-2)
#
#     res = max(cnt, cnt2)
#     ans = max(hap, hap2)
#
#     print(f'#{t} {ans} {res} {max(arr)} {dq.pop()+1}')


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    cnt = hap = 0
    arr = []
    ans = []
    for i in range(0,M,2):
        for j in range(N):
            arr.append(lst[j][i])
            cnt += 1
            hap += lst[j][i]

    for i in range(0,M,2):
        for j in range(N):
            if max(arr) == lst[j][i]:
                ans.append(i+1)

    print(f'#{t} {hap} {cnt} {max(arr)} {max(ans)}')