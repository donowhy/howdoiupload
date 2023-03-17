# c = dict()  # 딕셔너리에 키 벨류 저장할 수 있는데 #'A' : 2
# s = input()
#
# for ch in s:
#     if ch in c:
#         c[ch] += 1
#     else:
#         c[ch] = 1
#
# if sum(i % 2 for i in c.values()) > 1:
#     print("I'm Sorry Hansoo")
# else:
#     half = ''
#     for k, v in sorted(c.items()): #만약  A: 4개면 절반을 더해줌
#         half += k * (v//2)
#
#     ans = half
#     for k, v in c.items():
#         if v%2:
#             ans += k
#             break
#     ans += ''.join(reversed(half))
#     print(ans)


from collections import Counter

c = Counter(input())

if sum(i % 2 for i in c.values()) > 1:
    print("I'm Sorry Hansoo")
else:
    half = ''
    for k, v in sorted(c.items()): #만약  A: 4개면 절반을 더해줌
        half += k * (v//2)

    ans = half
    for k, v in c.items():
        if v%2:
            ans += k
            break
    ans += ''.join(reversed(half))
    print(ans)