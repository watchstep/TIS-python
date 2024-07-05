# 이진 검색 트리
import sys;input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

preord = []
while True:
    try:
        node = int(input())
        preord.append(node)
    except:
        break

def pre_to_post(left, right):
    if left > right:
        return
    root = preord[left]
    mid = right + 1 # 오른쪽 하위 트리가 없을 경우
    
    for i in range(left + 1, right + 1):
        if preord[i] > root: # root보다 큰 값이면 오른쪽 하위 트리의 첫 번째 원소
            mid = i
            break
        
    pre_to_post(left + 1, mid - 1) # 왼쪽
    pre_to_post(mid, right) # 오른쪽
    print(preord[left])
    
pre_to_post(0, len(preord) - 1)

