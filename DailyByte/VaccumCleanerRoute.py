""" 
This question is asked by Amazon. Given a string representing the sequence of moves a robot vacuum makes, 
return whether or not it will return to its original position. The string will only contain L, R, U, and D 
characters, representing left, right, up, and down respectively.
Ex: Given the following strings...
"LR", return true
"URURD", return false
"RUULLDRD", return true 
"""
def check(s):
    x,y=0,0
    for i in s:
        if i=='L':
            x+=1
        elif i=='R':
            x-=1
        elif i=='U':
            y+=1
        else:
            y-=1
    if x==0 and y==0:
        return True
    else:
        return False

if __name__=="__main__":
    for _ in range(int(input())):
        print(check(input()))