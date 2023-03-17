'''
N = int(input())
lst = list(map(int,input().split()))
student_num = int(input())

for i in range(student_num):
    a, b = map(int, input().split())
    if a == 1:
        num = N / b
        for j in range(1,num +1):
            if lst[num * j] == 0:
                lst[num * j] == 1
            else:
                lst[num * j] == 0

    else:
        for k in range(b-1):
            for l in range(b,len(lst)-(len(lst)-b)):
                lst[l-k] == lst[l+k]
'''

#방법 2
def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())
switch = [-1] + list(map(int, input().split()))
print(switch)
students = int(input())
for _ in range(students):
    sex, num = map(int, input().split())
    # 남자
    if sex == 1:
        for i in range(num, N + 1, num):
            change(i)
    # 여자
    else:
        change(num)
        for k in range(N // 2):
            if num + k > N or num - k < 1: break
            if switch[num + k] == switch[num - k]:
                change(num + k)
                change(num - k)
            else:
                break

for i in range(1, N + 1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()


#방법 3
N = int(input())
bit = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    gender, switch = map(int, input().split())

    if gender == 1:
        for i in range(1, (len(bit) // switch) + 1):
            if bit[(switch * i) - 1] == 0:
                bit[(switch * i) - 1] = 1
            else:
                bit[(switch * i) - 1] = 0

    if gender == 2:
        if bit[(switch - 1)] == 0:
            bit[(switch - 1)] = 1
        else:
            bit[(switch - 1)] = 0
        l = switch - 2
        r = switch
        while l >= 0 and r < N and bit[l] == bit[r]:
            if bit[l] == 0:
                bit[l], bit[r] = 1, 1
            elif bit[l] == 1:
                bit[l], bit[r] = 0, 0
            l -= 1
            r += 1
            if l < 0 or r >= N:
                break

cnt = 0
ans = ''
for i in range(N):
    ans += (str(bit[i]) + ' ')
    cnt += 1
    if cnt == 20:
        print(ans)
        ans = ''
        cnt = 0
if len(ans) != 0:
    print(ans)

#방법 4
switch_num = int(input())  # 스위치 개수
switch_status = list(map(int, input().split()))  # 스위치 상태
student_count = int(input())  # 학생수
student_status = []  # 학생 성별과 받은 스위치 값 저장
for i in range(student_count):
    student_status.append(list(map(int, input().split())))

for i in student_status:

    if i[0] == 1:  # 남자일때
        for j in range(len(switch_status)):
            if (j + 1) % i[1] == 0:  # 스위치의 인덱스 + 1 값이 학생이 받은 스위치의 번호와 같다면
                switch_status[j] = int(not switch_status[j])  # 그 값을 반대로 뒤집어 준다.
    else:  # 여자일때
        for j in range(len(switch_status)):
            if (j + 1) == i[1]:  # 스위치의 인덱스 + 1 값이 학생이 받은 스위치의 번호와 같다면
                plus = j + 1  # 그 다음 인덱스 저장
                minus = j - 1  # 그 전 인덱스 저장
                switch_status[j] = int(not switch_status[j])  # 우선 해당 인덱스의 스위치 값을 반대로
                while True:

                    if minus >= 0 and plus < len(switch_status):  # 만약 범위를 벗어나지 않는다면
                        if switch_status[minus] == switch_status[plus]:  # 만약 양쪽이 대칭이라면
                            switch_status[minus] = int(not switch_status[minus])  # 스위치 값을 반대로
                            switch_status[plus] = int(not switch_status[plus])  # 스위치 값을 반대로
                        else:  # 대칭이 아니라면
                            break  # 더돌 필요가 없으므로 break
                    else:  # 만약 범위를 벗어난다면
                        break  # 바로 탈출

                    minus -= 1  # 왼쪽 인덱스는 한칸더 왼쪽으로
                    plus += 1  # 오른쪽 인덱스는 한칸더 오른쪽으로

count = 0  # 20개 출력을 위한 변수 선언
while count < len(switch_status):

    print(switch_status[count], end=" ")
    if count % 20 == 19:
        print()
    count += 1