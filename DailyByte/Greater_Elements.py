def greater(a: list,b: list) -> list:
    res=[]
    for i in a:
        x=b.index(i)
        if x==len(b)-1 or i==max(b):
            res.append(-1)
            continue
        for j in range(x+1,len(b)):
            if i<b[j]:
                res.append(b[j])
                break
    return res

if __name__=="__main__":
    for _ in range(int(input())):
        a=list(map(int, input().split()))
        b=list(map(int, input().split()))
        print(greater(a,b))