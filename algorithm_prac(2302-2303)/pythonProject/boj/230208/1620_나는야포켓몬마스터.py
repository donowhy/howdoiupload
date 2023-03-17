# N, M = map(int,input().split())
#
# name_lst = []
# quiz_lst = []
#
# for i in range(N):
#     letter = input()
#     name_lst.append(letter)
# # print(name_lst)
#
# for i in range(M):
#     quiz = input()
#     quiz_lst.append(quiz)
# # print(quiz_lst)
#
# for i in range(M):
#     # print(quiz_lst[i])
#     if int(quiz_lst[i]):
#         print(name_lst[int(quiz_lst[i]) - 1])
#
#     for j in range(N):
#         try:
#             if quiz_lst[i] == name_lst[j]:
#                 print(j+1)
#         except:
#             if quiz_lst[i] == name_lst[j]:
#                 print(j+1)

#나랑 방법 똑 같은것
# import sys
# n, m = map(int, input().split())
#
# # 리스트에 포켓몬 저장
# poketlist = []
# for i in range(n):
#     temp = sys.stdin.readline().strip()
#     poketlist.append(temp)
#
# # 포켓몬 탐색
# for _ in range(m):
#     item = sys.stdin.readline().strip()
#     # 입력값이 int일 경우
#     if item.isdigit() == True:  # isdigit -> O(n)
#         print(poketlist[int(item)-1])
#     # 입력값이 int가 아닐 경우 (문자열일경우)
#     else:
#         print(poketlist.index(item))
# .strip()
#방법 2
import sys

n, m = map(int, input().split())

# 리스트에 포켓몬 저장
pokedic_int_key = {}  # Key값이 int인 dictionary
pokedic_name_key = {}  # Key값이 str인 dictionary
for i in range(n):
    name = sys.stdin.readline()
    pokedic_int_key[i] = name
    pokedic_name_key[name] = i

# 포켓몬 탐색
for _ in range(m):
    item = sys.stdin.readline()
    # 입력값이 int일 경우, key값이 int인 dictionary에서 value를 가져옴
    if item.isdigit() == True:  # isdigit -> O(n)
        print(pokedic_int_key[int(item)-1])
    # 입력값이 int가 아닐 경우 (문자열일경우), key값이 str인 dictionary에서 value를 가져옴
    else:
        print(pokedic_name_key[item]+1)