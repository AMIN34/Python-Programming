def longCommonPrefixUtil(s1,s2):
    res=""
    l1,l2,i,j=len(s1),len(s2),0,0
    while i<=l1-1 and j<=l2-1:
        if s1[i]!=s2[j]:
            break
        res += s1[i]
        i,j = i+1,j+1 
    return res

def longCommonPrefix(arr,low,high):
    if low == high:
        return arr[low]
    if low < high:
        mid = low + (high - low)//2
        s1=longCommonPrefix(arr,low,mid)
        s2=longCommonPrefix(arr,mid+1,high)
        return longCommonPrefixUtil(s1,s2)

if __name__=="__main__":
    for _ in range(int(input())):
        s=list(map(str,input().split()))
        result = longCommonPrefix(s,0,len(s)-1)
        print(result)