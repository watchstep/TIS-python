# 후보 추천하기
import sys;input=sys.stdin.readline
from collections import defaultdict

n = int(input()) # 사진틀 개수
rec_cnt = int(input()) # 총 추천 횟수
rec_students = list(map(int, input().split())) # 추천받은 학생 번호
rec_dict = defaultdict(int)

for student in rec_students:
  if student not in rec_dict and len(rec_dict) == n:
    delete_student = [k for k, v in rec_dict.items() if min(rec_dict.values()) == v][0]
    del rec_dict[delete_student]
  rec_dict[student] += 1
  
res = sorted(rec_dict)
print(*res)

### 다른 풀이
import sys;input=sys.stdin.readline
from collections import defaultdict

n = int(input()) # 사진틀 개수
rec_cnt = int(input()) # 총 추천 횟수
rec_students = list(map(int, input().split())) # 추천받은 학생 번호
rec_dict = defaultdict(int)

for student in rec_students:
  if student not in rec_dict and len(rec_dict) == n:
    keys = list(rec_dict.keys())
    vals = list(rec_dict.values())
    delete_student = keys[vals.index(min(vals))]
    del rec_dict[delete_student]
  rec_dict[student] += 1
  
res = sorted(rec_dict)
print(*res)

