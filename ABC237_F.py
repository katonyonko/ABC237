import io
import sys

_INPUT = """\
6
4 5
3 4
111 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,M=map(int,input().split())
  