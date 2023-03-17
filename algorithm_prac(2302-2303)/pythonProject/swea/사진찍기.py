import pprint

for t in range(1, int(input()) + 1):
    N, K, A, B = map(int, input().split())
    board = [input().split() for _ in range(N)]
    # pprint.pprint(board)
    arr_1 = []
    arr_2 = []
    ans = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                arr_1.append(i)
                arr_2.append(j)
    cnt = -1

    while K >= 1:
        if max(arr_1) - A <= K//2 and A - min(arr_1) <= + K//2 and max(arr_2) - B <= K//2 and B - min(arr_2) <= + K//2:
            ans.append(K)
            K -= 2
            cnt += 1
        else:
            break

    print(cnt)
'''
for t in range(1, int(input()) + 1):
    N, K, A, B = map(int, input().split())
    board = [input().split() for _ in range(N)]

    arr_1 = []
    arr_2 = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                arr_1.append(i)
                arr_2.append(j)

    cnt = -1

    while K >= 1:
        if max(arr_1) - A <= K//2 and A - min(arr_1) <= + K//2 and max(arr_2) - B <= K//2 and B - min(arr_2) <= + K//2:
            K -= 2
            cnt += 1
        else:
            break

    print(f'#{t} {cnt}')
'''
