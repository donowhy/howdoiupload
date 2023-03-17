# arr = [2,3,5,7]
#
# for i in range(2, 1001):
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i%11 !=0:
#         arr.append(i)
# print(arr)
# T = int(input())
#
# lst = list(map(int,input().split()))
# cnt =0
# for i in lst:
#     if i in arr:
#         cnt +=1
#
# print(cnt)


# n = int(input())
# nums = list(map(int, input().split()))
#
# cnt = 0
# for num in nums:
#     res = 0
#     if num > 1 :
#         for i in range(2, num):
#             if num % i == 0:
#                 res = 1
#         if res != 1:
#             cnt += 1
# print(cnt)


import sys
input = sys.stdin.readline
def dfs(lttr, idx):
    if lttr == l:
        mo = 0
        ja = 0
        for i in range(l):
            if arr[i] in 'aeiou':
                mo += 1
            else:
                ja += 1
        if mo >= 1 and ja >= 2:
            #자음과 모음이 조건에 맞으면
            print(''.join(arr))
        return #뒤로 돌아가기
    for i in range(idx, c):
        if check[i] == 0:
            arr.append(letter[i])
            check[i] = 1
            dfs(lttr + 1, i + 1)
            check[i] = 0
            del arr[-1]

l, c = map(int, input().split())
check = [0 for i in range(c)]
letter = input().split()
letter.sort()
arr = []
dfs(0, 0)