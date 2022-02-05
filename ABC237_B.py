import io
import sys

_INPUT = """\
6
4 3
1 2 3
4 5 6
7 8 9
10 11 12
2 2
1000000000 1000000000
1000000000 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  H,W=map(int,input().split())
  A=[list(map(int,input().split())) for _ in range(H)]
  B=[[A[j][i] for j in range(H)] for i in range(W)]
  for i in range(W):
    print(*B[i])