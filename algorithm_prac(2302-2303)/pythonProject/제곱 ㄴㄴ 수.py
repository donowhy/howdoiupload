

mn, mx = map(int,input().split())

i = 2
chk = [1] * (mx- mn + 1)
# print(chk)

while i ** 2 <= mx:
    tr = (mn // (i ** 2))
    while tr * (i ** 2) <= mx:
        if tr * (i ** 2) - mn >= 0 and tr * (i ** 2) - mn <= mx - mn:
            chk[tr * (i ** 2) - mn ] = 0
        tr += 1
    i += 1

print(sum(chk))



from math import isqrt
min,max=map(int,input().split())
chk=[1 for i in range(max-min+1)]
for i in range(2,isqrt(max)+1):
    sq=i*i
    for j in range(min+sq-min%sq if min%sq else min,max+1,sq):
        if(chk[j-min]):
            chk[j-min]=0
print(sum(chk))



MAX_NUM = int(1e6)
mu = [0 for _ in range(MAX_NUM + 10)]
mu[0] = None
mu[1] = 1

for i in range(1, MAX_NUM + 1):
    for j in range(2 * i, MAX_NUM + 1, i):
        mu[j] -= mu[i]

def count_SFI(n):
    cnt = 0
    i = 1
    while i ** 2 <= n:
        cnt += mu[i] * (n // (i ** 2))
        i += 1
    return cnt

min_n, max_n = map(int, input().split())
print(count_SFI(max_n) - count_SFI(min_n - 1))