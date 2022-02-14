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
  dp=[[[[0]*(M+1) for k in range(M+1)] for j in range(M+1)] for i in range(N+1)]
  dp[0][M][M][M]=1

  for i in range(N):
    for j in range(M+1):
      for k in range(M+1):
        for l in range(M+1):
          for m in range(M):
            if m<=j:
              dp[i+1][m][k][l]=(dp[i+1][m][k][l]+dp[i][j][k][l])%mod
            elif m<=k:
              dp[i+1][j][m][l]=(dp[i+1][j][m][l]+dp[i][j][k][l])%mod
            elif m<=l:
              dp[i+1][j][k][m]=(dp[i+1][j][k][m]+dp[i][j][k][l])%mod

  print(sum([sum([sum([dp[N][j][k][l] for l in range(M)]) for k in range(M)]) for j in range(M)])%mod)
    