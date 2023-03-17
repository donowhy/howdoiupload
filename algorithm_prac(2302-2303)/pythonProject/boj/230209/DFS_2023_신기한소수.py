# import sys
#
# sys.setrecursionlimit(1000)
# input = sys.stdin.readline
# N = int(input())
#
# def isPrime(num):
#     for i in range(2, int(num / 2 + 1)):
#         if num % i == 0:
#             return False
#         return True
#
# def dfs(number):
#     if len(str(number)) == N:
#         print(number)
#
#     else:
#         for i in range(1, 10):
#             if i % 2 == 0 or i % 5 == 0:
#                 continue
#             elif isPrime(number * 10 + i):
#                 dfs(number * 10 + i)
#
# dfs(2)
# dfs(3)
# dfs(5)
# dfs(7)


n = int(input())


# 소수 판별
def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if (a % i == 0):
            return False
    return True


def dfs(num):
    # 목표 길이 도달 시 멈춤
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if isPrime(temp):
                dfs(temp)


dfs(2)
dfs(3)
dfs(5)
dfs(7)
