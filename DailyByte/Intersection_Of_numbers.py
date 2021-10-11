def intersection(l1,l2):
    return list(set(l1) & set(l2))
def main():
    for _ in range(int(input())):
        l1=list(map(int, input().split()))
        l2=list(map(int, input().split()))
        print(intersection(l1,l2))
if __name__=="__main__":
    main()