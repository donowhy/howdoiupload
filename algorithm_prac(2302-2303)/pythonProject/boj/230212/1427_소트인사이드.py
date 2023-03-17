# import sys
# print = sys.stdout.write
#
# lst = list(input())
#
# for i in range(len(lst)):
#     max = i
#     for j in range(i + 1, len(lst)):
#         if lst[j] > lst[max]:
#             max = j
#
#     if lst[i] < lst[max]:
#         temp = lst[i]
#         lst[i] = lst[max]
#         lst[max] = temp
#
# for i in range(len(lst)):
#     print(lst[i])

lst = list(input())

lst.sort(reverse=True)

for i in range(len(lst)):
    print(lst[i], sep = '', end='')