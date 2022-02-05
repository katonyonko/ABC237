import io
import sys

_INPUT = """\
6
kasaka
atcoder
php
a
akaka
axa
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  N=len(S)
  idx=N-1
  x=0
  while idx>=0 and S[idx]=='a':
    x+=1
    idx-=1
  y=0
  idx=0
  while idx<N and S[idx]=='a':
    y+=1
    idx+=1
  S='a'*max(x-y,0)+S
  N=len(S)
  ans='Yes'
  for i in range(N):
    if S[i]!=S[N-1-i]: ans='No'
  print(ans)