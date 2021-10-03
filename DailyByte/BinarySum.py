def solve(s):
    s=s.split(" ")
    x,y=s[0],s[1]
    return bin(int(x,2)+int(y,2)).replace("0b","")

if __name__=="__main__":
    for _ in range(int(input())):
        print(solve(input()))
