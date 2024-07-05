# 폰 호석만
import sys;input=sys.stdin.readline

A, B = input().split()

cnt = 0
for i in range(2, 37):
    for j in range(2, 37):
        try:
            n1 = int(A, i)
            n2 = int(B, j)
            if n1 == n2 and i != j:
                cnt += 1
                tmp = [n1, i, j]
        except:
            continue

if cnt > 1:
    print('Multiple')
elif cnt == 1:
    print(*tmp)
else:
    print('Impossible')

#######################################
def to_num(str_x):
    res = ''
    for i in str_x:
        res += str(ord(i) - 87)
    return int(res)

def to_base(num, base):
    res = ''
    while num > 0:
        num, r = divmod(num, base)
        res = str(r) + res # res += str(r) ㄴㄴ 이전 문자열 뒤에 붙게 되므로
    return int(res)

# n진수 -> 10진수
# str로 받으면 바로
def to_10(num, base):
    res = 0
    power = 0
    while num > 0:
        num, r = divmod(num, 10)
        res += r*(base**power) 
        power += 1
    return res
# 8진수 345 -> 5*8^0 + 4*8^1 + 3*8^2 
to_10(1425, 32) # 왜 473이 아니라 36933이 나올까...
to_10(345, 8)
int('ep', 32)
to_num('ep')