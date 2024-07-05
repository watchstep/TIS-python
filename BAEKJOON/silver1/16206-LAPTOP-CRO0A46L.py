# 롤케이크
import sys;input = sys.stdin.readline

N, M = map(int, input().split())
roll = sorted(list(map(int, input().split()))) # 오름차순 정렬
roll.sort(key=lambda x: x%10) # 10의 배수가 앞으로 오도록 다시 정렬

cnt = 0

for r in roll:
    if M > 0:
        q, r = divmod(r, 10) # 몫, 나머지
        if r == 0: # 10의 배수인 경우
            if q - 1 == 0: # 10일 경우
                cnt += 1
            else:
                if M >= q - 1:
                    cnt += q # ex) 20 한 번만 잘라도 10, 10 2개의 롤케이크
                    M -= q - 1
                else:
                    cnt += M
                    break
        else: # 10의 배수가 아닌 경우
            if M >= q:
                cnt += q  # ex) 23 한 번 자르면 10, 13 1개의 롤케이크 2번 잘라야 10, 10, 3 2개의 롤케이크
                M -= q
            else:
                cnt += M
                break
    else:
        break            

print(cnt)

# https://art-coding3.tistory.com/51



