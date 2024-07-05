# 트리
import sys;input=sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    
    

# 후위 순회
# 왼 - 오 - 루트
