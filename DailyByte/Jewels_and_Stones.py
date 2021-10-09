def count(j,s):
    c=0
    for i in j:
        c += s.count(i)
    return c
if __name__=="__main__":
    for _ in range(int(input())):
        j=list(map(str, input()))
        s=list(map(str, input()))
        print(count(j,s))