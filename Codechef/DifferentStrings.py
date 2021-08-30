for _ in range(int(input())):
    n=int(input())
    arr=[input() for i in range(n)]
    sol=""
    for i in range(n):
        if arr[i][i]=="0":
            sol+="1"
        else:
            sol+="0"
    print(sol)
    """ m=max(arr)
    m=int(m,2)
    m+=1
    print(bin(m).replace("0b","")) """