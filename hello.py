print("Hello World")
from sympy import symbols,Eq,solve
x,y=symbols('x y')
equation1=Eq(4*x-2*y-2,0)
equation2=Eq(x-y,0)
solution=solve((equation1,equation2),(x,y))
print(solution)