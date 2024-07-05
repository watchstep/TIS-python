# 멍멍이 쓰다듬기
import sys;input=sys.stdin.readline
import math 
x, y = map(int, input().split())
diff = y - x 

# 애초에 원숭이와 멍멍이 키 같을 때
if diff == 0:
    print(0)
elif diff == 1:
    print(1)
elif diff == 2:
    print(2)
else:
    n = int(math.sqrt(diff))
    if n**2 == diff:
        print(n*2 - 1)
    else:
        m = diff - n**2
        if m <= n:
            print(n*2)
        else:
            print(n*2 + 1)