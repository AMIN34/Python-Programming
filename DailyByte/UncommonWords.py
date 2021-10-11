def uncWords(s1,s2):
    s1= (s1+" "+s2).split(" ")
    d={}
    res=[]
    for i in s1:
        d[i]=d.get(i,0)+1
    for keys,values in d.items():
        if values==1:
            res.append(keys)
    return res

def main():
    for _ in range(int(input())):
        s1 = input()
        s2 = input()
        print(uncWords(s1,s2))
if __name__=="__main__":
    main()