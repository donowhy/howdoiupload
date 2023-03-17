# letter = list(input())
# stk = []
# res = ''
#
# for i in letter:
#     if i.isalpha():
#         res += i
#     else:
#         if i == '(':
#             stk.append(i)
#         elif i == '*' or i == '/':
#             while stk and (stk[-1] == '*' or stk[-1] == '/'):
#                 res += stk.pop()
#             stk.append(i)
#         elif i == '+' or i == '-':
#             while stk and stk[-1] != '(':
#                 res += stk.pop()
#             stk.append(i)
#         elif i == ')':
#             while stk and stk[-1] != '(':
#                 res += stk.pop()
#             stk.pop()
# while stk:
#     res += stk.pop()
# print(res)
# #
# #
# # import sys
# #
# #
# # def postfix(post):
# #     stack = list()
# #
# #     for i in range(len(post) - 1):
# #         if (post[i] == "("):
# #             stack.append(post[i])
# #         elif (post[i] == "+" or post[i] == "-"):
# #             while(stack and stack[-1]!='('):
# #                 print(stack.pop(), end="")
# #             stack.append(post[i])
# #         elif (post[i] == "*" or post[i] == "/"):
# #             while (stack and stack[-1] != '(' and (stack[-1] == "*" or stack[-1] =='/')):
# #                 print(stack.pop(), end="")
# #             stack.append(post[i])
# #         elif (post[i] == ")"):
# #             while (stack and stack[-1] != '('):
# #                 print(stack.pop(), end="")
# #             stack.pop()
# #         elif (post[i] >= 'A' and post[i] <= 'Z'):
# #             print(post[i], end="")
# #
# #     if (len(stack) >0):
# #         for i in range(len(stack)):
# #             print(stack.pop(), end="")
# #
# #
# # post = sys.stdin.readline()
# # postfix(post)
# #
# #
# #
# # num = input()
# # answer = ''
# # stack = []
# #
# # for i in num:
# #     if i.isalpha():
# #         answer += i
# #     else:
# #         if i == '(':
# #             stack.append(i)
# #
# #         elif i == '*' or i == '/':
# #             while stack and (stack[-1] == '*' or stack[-1] == '/'):
# #                 answer += stack.pop()
# #             stack.append(i)
# #
# #         elif i == '+' or i == '-':
# #             while stack and stack[-1] != '(':
# #                 answer += stack.pop()
# #             stack.append(i)
# #
# #         elif i == ')':
# #             while stack and stack[-1] != '(':
# #                 answer += stack.pop()
# #             stack.pop()
# #
# # while stack:
# #     answer += stack.pop()
# #
# # print(answer)
# #
# #
# # I = list(input())
# #
# # stk = []
# # arr = ('+', '-', '*', '/', '(', ')')
# # sik = []
# # res = ''
# # while I:
# #     let = I.pop(0)
# #     if let.isalpha():
# #         res += let
# #     if let in arr:
# #         print(sik)
# #         if sik:
# #             if sik[-1] == '*' or stk[-1] == '/':
# #                 if let == '-' or let == '+':
# #                     sik.append(let)
# #             elif sik[-1] == '+' or stk[-1] == '-':
# #                 sik.append(let)
# #         else:
# #             sik.append(let)
# # print(res, sik)
# #
# #
# #
# #
# #
# #
# #
# #


import sys


def solution(n, graph):
    dp = [[0] * 3 for _ in range(n)]

    dp[1][0] = graph[1][0] + graph[0][1]
    dp[1][1] = graph[1][1] + min(dp[1][0], graph[0][1], graph[0][2]+graph[0][1])
    dp[1][2] = graph[1][2] + min(dp[1][1], graph[0][1], graph[0][1] + graph[0][2])

    for i in range(2, n):
        for j in range(3):
            if j == 0:
                min_value = min(dp[i - 1][j], dp[i - 1][j + 1])
            elif j == 1:
                min_value = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1], dp[i][j - 1])
            else:
                min_value = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

            dp[i][j] = min_value + graph[i][j]

    print(f'{tc}. {dp[-1][1]}')
tc = 0
while True:
    a = int(input())
    if a == 0:
        break
    b = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
    tc += 1
    solution(a, b)