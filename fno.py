from math import gcd, factorial, floor, ceil
from fractions import Fraction
import operator as op
from functools import reduce

def nCr(n, r):
  r = min(r, n-r)
  number = reduce(op.mul, range(n, n-r, -1), 1)
  deno = reduce(op.mul, range(1, r+1), 1)
  return Fraction(number, deno)

T = int(input().strip())
for _ in range(T):
  A, H, L1, L2, M, C = tuple(map(int,input().strip().split()))
  sn, L = ceil((H-M*A)/C), Fraction(L1,L2)

  c = Fraction(0)
  for k in range(sn,M+1):
    c += nCr(M,k)*L**k*(1-L)**(M-k)

  p1,p2 = c.numberator, c. denoinaqtor
  if p1==0:
    print('RIP')
  else:
    _ = gcd(p1,p2)
    print('{}/{}'.format(p1//_,p2//_))