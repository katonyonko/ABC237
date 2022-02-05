import io
import sys

_INPUT = """\
6
5
LRRLR
7
LLLLLLL
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from collections import deque
  N=int(input())
  A=deque([N])
  S=input()
  for i in reversed(range(N)):
    if S[i]=='L':
      A.append(i)
    else:
      A.appendleft(i)
  print(*A)