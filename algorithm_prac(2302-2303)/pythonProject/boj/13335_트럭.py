# from collections import deque
# dq = arr = deque
# dq = []
#
# n, w, l = map(int,input().split())
#
# lst = list(map(int,input().split()))
# cnt = 0
# while len(lst) >= 1:
#     hap=0
#     for i in range(len(lst)):
#         if hap < l:
#             hap += lst[i]
#         elif hap >= l:
#             lst.pop(0) * (i -1)
#             cnt += w
#             exit()
#
#         # print(hap)
#
#
# print(cnt)
#
# n, w, l = map(int, input().split())
# q = list(map(int, input().split()))
#
# b = [0] * w
# time = 0
# while b:  # 마지막 트럭이 들어오고 그 트럭이 빠져나갈 때 까지
#     time += 1
#     b.pop(0)  # 다리 첫번째 요소 pop
#     if q:  # 트럭이 존재할 때만 다리에 append
#         if sum(b) + q[0] <= l:
#             b.append(q.pop(0))
#         else:
#             b.append(0)  # 트럭이 있지만 다리에 올리지 못할 경우 다리 공간 채워줘야 함
# print(time)




# import sys
# from _collections import deque
# input = sys.stdin.readline
#
# N, W, L = map(int, input().split())
# trucks = deque(list(map(int, input().split())))
#
# answer = 0
# bridge = deque([0 for _ in range(W)])
# print(bridge)
#
# while trucks:
#     bridge.popleft()
#     print(bridge,'popleft')
#     if len(bridge) < W:
#         if sum(bridge) + trucks[0] <= L:
#             truck = trucks.popleft()
#             print(truck,'트럭')
#             bridge.append(truck)
#             print(bridge, '브릿지')
#         else:
#             bridge.append(0)
#             print(bridge,'append')
#     answer += 1
#     print(answer,'cnt')
# answer += W
# print(answer)

from collections import deque

N, K = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
while K > 0:
    A.append(A.pop(0)-1)
    cnt += 1
    if A[0] - 1 == 0:
        K -= 1
print(cnt)

import sys

input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
res = 0

while 1:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 로봇이 내려가는 부분이니 0
    if sum(robot):  # 로봇이 존재하면
        for i in range(n - 2, -1, -1):  # 로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터
            if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
        robot[-1] = 0  # 이 부분도 로봇 out -> 0임
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    res += 1
    if belt.count(0) >= k:
        break

print(res)



from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split()))  # 내구도. A1, A2, ..., A2N
robot = deque([0] * n)  # 벨트위에 있는 로봇
result = 0

while True:
    result += 1
    # 1. 벨트 회전한다.
    a.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0    # 내리는 위치에 도달한 경우, 즉시 내림
    # 2. 로봇 이동하기. 이동하려는 칸에 로봇 x, 내구도 1이상 남아야함.
    for i in range(n - 2, -1, -1):  # 먼저 올라간 로봇부터 진행
        if a[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            a[i + 1] -= 1
    robot[-1] = 0  # 내리는 위치에 도달한 경우, 즉시 내림
    # 3. 올리는 위치에 내구도 0 아니면 로봇 올리기 & 내구도 감소
    if a[0] != 0 and robot[0] != 1:
        robot[0] = 1
        a[0] -= 1
    # 4. 내구도 0인 칸 수가 k이상이면 종료
    if a.count(0) >= k:
        break
print(result)