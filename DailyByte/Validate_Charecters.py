def validate(s: str) -> bool:
    x=y=z=0
    for i in s:
        if i=='(':
            x+=1
        elif i=='{':
            y+=1
        elif i=='[':
            z+=1
        elif i==')':
            x-=1
        elif i=='}':
            y-=1
        elif i==']':
            z-=1
        else:
            continue
    if x and y and z:
        return False
    return True

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        print(validate(s))