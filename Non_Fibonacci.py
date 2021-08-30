def nonFibonacci(n):
    prevPrev=1
    prev=2
    curr=3
    while n> 0:
        prevPrev=prev
        prev=curr
        curr+=prevPrev+prev
        n-=(curr-prev-1)
    n+=  curr -prev -1
    return prev+n

def  main():
    n=int(input())
    print(nonFibonacci(n))

if __name__=="__main__":
    main()