# 회문
import sys;input=sys.stdin.readline

def is_palindrome(s):
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] != s[end]:
            # 바로 뒷문자 삭제했을 때 회문인지
            if s[start] == s[end - 1]:
                tmp = s[start:end]
                if tmp[:] == tmp[::-1]:
                    return 1
            # 바로 앞문자 삭제했을 때 회문인지
            if s[start + 1] == s[end]:
                tmp = s[start + 1:end + 1]
                if tmp[:] == tmp[::-1]:
                    return 1
            return 2
        else:
            start += 1
            end -= 1
    return 0
            
T = int(input())
for _ in range(T):
    s = input().rstrip()
    print(is_palindrome(s))
    