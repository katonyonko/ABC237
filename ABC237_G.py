import io
import sys

_INPUT = """\
6
5 2 1
1 4 5 2 3
1 3 5
2 1 3
7 3 3
7 5 3 1 2 4 6
1 1 7
2 3 6
2 5 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  class LazySegTree:
    X_unit = (0,0)
    A_unit = -2

    @classmethod
    def X_f(cls, x, y):
        return (x[0]+y[0],x[1]+y[1])

    @classmethod
    def A_f(cls, x, y):
        if y==-2: return x
        return y

    @classmethod
    def operate(cls, x, y):
        if y==-2: return x
        return (y*x[1],x[1])

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)
        self.A = [self.A_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def _eval_at(self, i):
        return self.operate(self.X[i], self.A[i])

    def _propagate_at(self, i):
        self.X[i] = self._eval_at(i)
        self.A[i << 1] = self.A_f(self.A[i << 1], self.A[i])
        self.A[i << 1 | 1] = self.A_f(self.A[i << 1 | 1], self.A[i])
        self.A[i] = self.A_unit

    def _propagate_above(self, i):
        H = i.bit_length() - 1
        for h in range(H, 0, -1):
            self._propagate_at(i >> h)

    def _recalc_above(self, i):
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self._eval_at(i << 1), self._eval_at(i << 1 | 1))

    def set_val(self, i, x):
        i += self.N
        self._propagate_above(i)
        self.X[i] = x
        self.A[i] = self.A_unit
        self._recalc_above(i)

    def fold(self, L, R):
        L += self.N
        R += self.N
        self._propagate_above(L // (L & -L))
        self._propagate_above(R // (R & -R) - 1)
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self._eval_at(L))
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self._eval_at(R), vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

    def operate_range(self, L, R, x):
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self._propagate_above(L0)
        self._propagate_above(R0)
        while L < R:
            if L & 1:
                self.A[L] = self.A_f(self.A[L], x)
                L += 1
            if R & 1:
                R -= 1
                self.A[R] = self.A_f(self.A[R], x)
            L >>= 1
            R >>= 1
        self._recalc_above(L0)
        self._recalc_above(R0)

  N,Q,X=map(int,input().split())
  P=list(map(int,input().split()))
  lst=LazySegTree(N)
  lst.build([(0,1) if P[i]==X else (1,1) if P[i]>X else (-1,1) for i in range(N)])
  ans=P.index(X)
  for _ in range(Q):
    C,L,R=map(int,input().split())
    if L<=ans+1<=R: inc=1
    else: inc=0
    s=lst.fold(L-1,R)[0]
    n=(R-L+1-s)//2
    p=R-L+1-n-(1 if inc==1 else 0)
    if C==1:
      lst.operate_range(L-1,L-1+n,-1)
      if inc==1:
        lst.operate_range(L-1+n,L+n,0)
        ans=L-1+n
      lst.operate_range(R-p,R,1)
    else:
      lst.operate_range(L-1,L-1+p,1)
      if inc==1:
        lst.operate_range(L-1+p,L+p,0)
        ans=L-1+p
      lst.operate_range(R-n,R,-1)
  print(ans+1)