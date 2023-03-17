# import sys
# input = sys.stdin.readline
#
# while True:
#     T = int(input().rstrip())
#     if T == 0:
#         break
#     if T % 2 == 0:
#         lst = [2, 3, 5, 7]
#         arr = []
#         for i in range(8, T):
#             if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
#                 lst.append(i)
#
#         for i in range(len(lst)//2 + 1):
#             for j in range(len(lst) - 1,len(lst)//2 - 1, -1):
#                 if lst[i] + lst[j] == T and len(arr) == 0:
#                     arr.append([lst[i], lst[j]])
#
#
#         if arr:
#             print(f'{T} = {arr[0][0]} + {arr[0][1]}')
#         else:
#             print("Goldbach's conjecture is wrong.")
#     else:
#         print("Goldbach's conjecture is wrong.")

# import sys
# input = sys.stdin.readline
#
# while True:
#     T = int(input().rstrip())
#     if T == 0:
#         break
#     if T % 2 == 0 and T >= 20:
#         if (T - 2) % 2 and (T - 2) % 3 and (T - 2) % 5 and (T - 2) % 7:
#             print(f'{T} = 2 + {T - 2}')
#
#         elif (T - 3) % 2 and (T - 3) % 3 and (T - 3) % 5 and (T - 3) % 7:
#             print(f'{T} = 3 + {T - 3}')
#
#         elif (T - 5) % 2 and (T - 5) % 3 and (T - 5) % 5 and (T - 5) % 7:
#             print(f'{T} = 5 + {T - 5}')
#
#         elif (T - 7) % 2 and (T - 7) % 3 and (T - 7) % 5 and (T - 7) % 7:
#             print(f'{T} = 7 + {T - 7}')
#         else:
#             print("Goldbach's conjecture is wrong.")
#
#     elif T % 2 == 0 and T < 20:
#         lst = [2, 3, 5, 7]
#         arr = []
#         for i in range(8, T):
#             if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
#                 lst.append(i)
#
#         for i in range(len(lst)//2 + 1):
#             for j in range(len(lst) - 1,len(lst)//2 - 1, -1):
#                 if lst[i] + lst[j] == T and len(arr) == 0:
#                     arr.append([lst[i], lst[j]])
#         if arr:
#             print(f'{T} = {arr[0][0]} + {arr[0][1]}')
#         else:
#             print("Goldbach's conjecture is wrong.")
#
#     else:
#         print("Goldbach's conjecture is wrong.")
#
#
#
#
#
#
#
#
#
#
#
#
#
# from sys import stdin
#
# array = [True for i in range(1000001)]
#
# for i in range(2, 1001):
#     if array[i]:
#         for k in range(i + i, 1000001, i):
#             array[k] = False
#
# while True:
#     n = int(stdin.readline())
#
#     if n == 0: break
#
#     for i in range(3, len(array)):
#         if array[i] and array[n - i]:
#             print(n, "=", i, "+", n - i)
#             break
#
#
#
#
#
#
#
#
#
#
#
#
#
# import sys
#
#
# def Goldbach():
#     check = [False, False] + [True] * 1000000
#
#     for i in range(2, 1001):
#         if check[i] == True:
#             for j in range(i + i, 1000001, i):
#                 check[j] = False
#
#     while True:
#         n = int(sys.stdin.readline())
#
#         if n == 0:
#             break
#
#         A = 0
#         B = n
#         for _ in range(1000000):
#             if check[A] and check[B]:
#                 print(f"{n} = {A} + {B}")
#                 break
#             A += 1
#             B -= 1
#         else:
#             print("Goldbach's conjecture is wrong.")
#
#
# Goldbach()