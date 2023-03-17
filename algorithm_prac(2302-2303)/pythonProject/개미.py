w, h = map(int, input().split())
p, q = map(int, input().split()) #가로 , 세로
t = int(input())
col = h - q
lst = [[p, col]]

while p < w  and 1 <= col:
    p += 1
    col -= 1
    lst.append([p, col])
print(lst)
while len(lst) < t:
    if p == w:
        while 0 < p and 0 < col < h:
            if lst[-1][0] > lst[-2][0] and lst[-1][1] < lst[-2][1]:
                p -= 1
                col -= 1
                lst.append([p,col])

            elif lst[-1][1] > lst[-2][1]:
                p += 1
                col += 1
                lst.append([p,col])


    if col == 0:
        while 0 < p < w and 0 <= col < h:
            if lst[-1][0] < lst[-2][0]:
                p -= 1
                col += 1
                lst.append([p,col])

            elif lst[-1][0] > lst[-2][0]:
                p += 1
                col -= 1
                lst.append([p,col])


    if col == h:
        while 0 < p < w and 0 < col <= h:
            if lst[-1][0] < lst[-2][0]:
                p -= 1
                col -= 1
                lst.append([p,col])

            elif lst[-1][0] > lst[-2][0]:
                p += 1
                col += 1
                lst.append([p,col])


    if p == 0:
        while 0 <= p < w and 0 < col < h:
            if lst[-1][1] < lst[-2][1]:
                p += 1
                col -= 1
                lst.append([p,col])
            elif lst[-1][1] > lst[-2][1]:
                p -= 1
                col += 1
                lst.append([p,col])

    if p == w and col == 0:
        while 0 < p <= w and 0 <= col < h:
            if lst[-1][0] < lst[-2][0]:
                p -= 1
                col += 1
                lst.append([p,col])
    if p == 0 and col == h:
        while 0 <= p < w and 0 < col <= h:
            if lst[-1][1] > lst[-2][1]:
                p += 1
                col -= 1
                lst.append([p, col])

    print(lst)
print(lst[t][0], abs(lst[t][1] - h))
