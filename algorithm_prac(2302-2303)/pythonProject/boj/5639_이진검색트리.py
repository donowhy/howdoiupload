# from collections import deque
# lst = deque()
# lst = [0] * 20
# arr = deque()
#
# while True:
#     try:
#         arr.append(int(input()))
#     except:
#         break
#
# lst[1] = arr[0]
#
# print(arr)
# for i in range(1, len(arr)-1):
#     if arr[0] > arr[i]:
#         if arr[i] < arr[i-1]:
#             lst[2 * i] = arr[i]
#         elif arr[i] > arr[i-1]:
#             lst[2*i+1] = arr[i]
#     else:
#         if arr[i] > arr[i + 1]:
#             lst[2 * i] = arr[i]
#         elif arr[i] < arr[i + 1]:
#             lst[2 * i + 1] = arr[i]
#
# print(lst)
# # def


import sys

sys.setrecursionlimit(10 ** 6)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break


def postorder(first, end):
    if first > end:
        return
    mid = end + 1  # 루트보다 큰 값이 존재하지 않을 경우를 대비
    for i in range(first + 1, end + 1):
        if num_list[first] < num_list[i]:
            mid = i
            break

    postorder(first + 1, mid - 1)
    postorder(mid, end)
    print(num_list[first])


postorder(0, len(num_list) - 1)



####
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(20_000)

def sort_tree(josang,start,end):
    if start >= N or start > end:
        return
    for idx in range(start+1,end+1):
        if nums[idx] > nums[start]:
            break
    else:
        idx = end + 1
    sort_tree(josang*2,start+1,idx-1)
    sort_tree(josang*2+1,idx,end)
    print(nums[start])

nums = list(map(int,sys.stdin.readlines()))
N = len(nums)
sort_tree(1,0,N-1)