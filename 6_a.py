import numpy as np 
A=[]
B=[]
print("Enter the elements for A in row-wise")
for i in range(3):  
    A.append([int(j) for j in input().split()])
print("Enter the elements for B in row-wise")
for i in range(3):  
    B.append([int(j) for j in input().split()])

result= []
result = np.dot(A,B)
for r in result: 
	print(r)
