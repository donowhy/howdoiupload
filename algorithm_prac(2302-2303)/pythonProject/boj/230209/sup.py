import sys
sys.stdin = open('sys.path/'+'input.txt','r')
# 17425 번 약수의 합
def yak(num):
    if lst.get(num):
        return lst.get(num)
    total = num + 1
    cha = [True] * (int(num ** 0.5) + 1)
    for i in range(2, int(num ** 0.5) + 1):
        if cha[i]:  # 약수라면
            if num % i == 0:  # 나눠진다면
                if int(num ** 0.5) == num ** 0.5:
                    total += i
                else:
                    total += i + (num // i)  # 나누는 수와, 몫
            else:  # 소수로 안나눠진다면 그 소수의 배수 또한 약수 X
                for j in range(i, int(num ** 0.5) + 1, i):
                    cha[j] == False

    return total


lst = {1: 1, 2: 4}
t = int(input())
for _ in range(t):
    n = int(input())
    if lst.get(n) is None:
        for i in range(3, n + 1):
            if lst.get(i) is None:
                lst[i] = yak(i) + lst[i - 1]
    print(lst[n])