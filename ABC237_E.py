import io
import sys

_INPUT = """\
6
4 4
10 8 12 5
1 2
1 3
2 3
3 4
2 1
0 10
1 2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #dijkstra
  from heapq import heappop,heappush
  def Dijkstra(G,s):
    done=[False]*len(G)
    inf=10**20
    C=[inf]*len(G)
    C[s]=0
    h=[]
    heappush(h,(0,s))
    while h:
      x,y=heappop(h)
      if done[y]:
        continue
      done[y]=True
      for v in G[y]:
        if C[v[1]]>C[y]+v[0]:
          C[v[1]]=C[y]+v[0]
          heappush(h,(C[v[1]],v[1]))
    return C
  
  N,M=map(int,input().split())
  H=list(map(int,input().split()))
  G=[[] for _ in range(N)]
  for i in range(M):
    u,v=map(int,input().split())
    u-=1; v-=1
    if H[u]>H[v]: u,v=v,u
    G[u].append(((H[v]-H[u]),v))
    G[v].append((0,u))
  C=Dijkstra(G,0)
  print(max([H[0]-H[i]-C[i] for i in range(N)]))