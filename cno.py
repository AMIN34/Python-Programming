'''LH  = int(input().strip())
UH  = int(input().strip())
LW  = int(input().strip())
UW  = int(input().strip())

dc = {}
ml = 0
counting = 0



def f(x,y):
  global  counting, ml
  counting += 1
  if x<y:
    x, y = y,x
  if x==0 or y==0:
    return 0
  if x==y:
    return 1
  else:
   
    if (x,y) not in dc:
      dc[(x,y)] = 1+f(x-y,y)
      if len(dc)>ml: ml = len(dc)
      if ((x-y,y) in dc): del dc[(x-y,y)]
    return dc[(x,y)]
   




result = 0
for i in range(LH,UH+1):
  for j in range(LW,UW+1):
    result += f(i,j)

print(result)'''

'''def count(a,b):
  minm=min(a,b)
  maxm=max(a,b)
  i=(minimum,maximum)
  if i in D:
    return D[i]
  if minm==0:
    return 0
  if minm==1:
    return a*b
  choco=maxm//minm
  newside=maxm%minm
  choco+=count(newside,minm)
  D[i]=choco
  return choco
D={}
p=int(input())
q=int(input())
r=int(input())
s=int(input())
ans=0
for i in range(p,q+1):
  for j in range(r,s+1):
    ans+=count(i,j)
print(ans)'''

def cntfr(a,b):
  maxs=max(a,b)
  mins=min(a,b)
  if mins==0:
    return 0
  if mins==1:
    return a*b
  t=maxs//mins
  ns=maxs%mins
  t=t+cntfr(ns,mins)
  return t
t=int(input())
for _ in range(t):
  p,q,r,s=list(map(int, input().split()))
  ans=0
  for i in range(p,q+1):
    for j in range(r,s+1):
      ans+=cntfr(i,j)
  print(ans)