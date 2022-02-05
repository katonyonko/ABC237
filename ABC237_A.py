import io
import sys

_INPUT = """\
6
10
-9876543210
483597848400000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  if -(1<<31)<=N<(1<<31):
    print('Yes')
  else:
    print('No')