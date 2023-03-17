# #dr: 북 동 남 서
# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]
# def solve(ci, cj, dr):
#     cnt = 0  #청소한 장소 수
#     while 1: # 청소기가 더 이상 움직이지 못 할때 종료
#         #[1] 현재위치 청소
#         arr[ci][cj] = 2 #1번 위치
#         cnt += 1
#
#         # [2] 왼쪽방향으로 순서대로 탐색해서 미청소 영역이 있으면 그 쪽으로 이동
#         flag = 1
#         while flag == 1:
#             # 왼쪽부터 네 방향으로 탐색 후 미청소 영역이 이 ㅆ는 경우
#             for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, (dr)): #왼쪽부터 순서대로 네 방향
#                 ni, nj = ci + di[nd], cj + dj[nd]
#                 if arr[ni][nj] == 0: #미청소 영역
#                     ci,cj,dr = ni,nj,nd
#                     flag = 0
#                     break
#
#             else: #for - else문 , 네 방향 모두 미청소 영역 없음 --> 후진
#                 bi,bj = ci-di[dr], cj-dj[dr] #후진
#                 if arr[bi][bj] == 1:    #벽이라면 종료
#                     return cnt
#                 else:
#                     ci, cj = bi, bj
#
# N, M = map(int,input().split())
# si, sj, dr = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
#
# ans = solve(si, sj, dr)
# print(ans)

# #dr: 북 동 남 서
# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]
# def solve(ci, cj, dr):
#     global cnt  #청소한 장소 수
#     while 1: # 청소기가 더 이상 움직이지 못 할때 종료
#         #[1] 현재위치 청소
#         arr[ci][cj] = 2 #1번 위치
#         cnt += 1
#
#         # [2] 왼쪽방향으로 순서대로 탐색해서 미청소 영역이 있으면 그 쪽으로 이동
#         flag = 1
#         while flag == 1:
#             # 왼쪽부터 네 방향으로 탐색 후 미청소 영역이 있는 경우
#             for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, (dr)): #왼쪽부터 순서대로 네 방향
#                 ni, nj = ci + di[nd], cj + dj[nd]
#                 if arr[ni][nj] == 0: #미청소 영역
#                     ci,cj,dr = ni,nj,nd  # 로봇의 위치 갱신, direction 갱신
#                     flag = 0  # False 로 만들고 탈출 다시 위로 가기
#                     break
#
#             else: #for - else문 , 네 방향 모두 미청소 영역 없음 --> 후진
#                 bi,bj = ci-di[dr], cj-dj[dr] #후진
#                 if arr[bi][bj] == 1:         #벽이라면 종료
#                     return cnt
#                 else:
#                     ci, cj = bi, bj
#
# N, M = map(int,input().split())
# si, sj, dr = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# cnt = 0
# solve(si, sj, dr)
# print(cnt)
#






# #수열
# n = int(input())
# stack = []
# answer = []
# cur = 1
# for i in range(n):
#     num = int(input())
#     while cur <= num:       # 입력한 수를 만날 때 까지 오름차순으로 push
#         stack.append(cur)
#         answer.append("+")
#         cur += 1
#     # 입력한 수를 만나면 while문 탈출. 즉 cur = num일 때 까지 while문을 돌아 스택을 쌓는다.
#
#     if stack[-1] == num:    # stack의 TOP이 입력한 숫자와 같다면
#         stack.pop()         # 스택의 TOP을 꺼내 수열을 만들어 준다.
#         answer.append("-")
#     else:                   # stack의 TOP이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
#         print("NO")         # 왜냐하면 12345 처럼 오름차순으로 스택이 입력되는데 TOP이 num보다 크면 num은 TOP보다 더 아래에 쌓여있기 때문이다.
#         exit()
#
#
# for i in answer:
#     print(i)

'''
5
6 9 5 7 4
'''

import sys

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
goto = [0] * n

for i in range(n):
    t = tower[i]
    while stack and tower[stack[-1]] < t:
        stack.pop()
        print(stack,'stack pop')
    if stack:
        goto[i] = stack[-1] + 1
        print(goto, 'goto')
    stack.append(i)
    print(stack, 'stack append')

print(' '.join(list(map(str, goto))))

