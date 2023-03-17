N, r, c = map(int, input().split())

ans = 0

while N != 0:

    N -= 1

    # 1사분면
    if r < 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 0

    # 2사분면
    elif r < 2 ** N and c >= 2 ** N:
        ans += (2 ** N) * (2 ** N) * 1
        c -= (2 ** N)

    # 3사분면
    elif r >= 2 ** N and c < 2 ** N:
        ans += (2 ** N) * (2 ** N) * 2
        r -= (2 ** N)

    # 4사분면
    else:
        ans += (2 ** N) * (2 ** N) * 3
        r -= (2 ** N)
        c -= (2 ** N)

print(ans)





import sys


def dc(x, y, n):
    global cnt
    if x > r or x + n <= r or y > c or y + n <= c:
        cnt += n ** 2
        return

    if n > 2:
        n //= 2
        dc(x, y, n)
        dc(x, y + n, n)
        dc(x + n, y, n)
        dc(x + n, y + n, n)
    else:
        if x == r and y == c:
            print(cnt)
        elif x == r and y + 1 == c:
            print(cnt + 1)
        elif x + 1 == r and y == c:
            print(cnt + 2)
        else:
            print(cnt + 3)
        sys.exit()


n, r, c = map(int, input().split())
cnt = 0
dc(0, 0, 2 ** n)







N, r, c = map(int, input().split())
cnt = 0

while N > 1:
    size = (2 ** N) // 2
    if r < size and c < size: # 2사분면
        pass
    elif r < size and c >= size: # 1사분면
        cnt += size ** 2
        c -= size
    elif r >= size and c < size: # 3사분면
        cnt += size ** 2 * 2
        r -= size
    elif r >= size and c >= size: # 4사분면
        cnt += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)
