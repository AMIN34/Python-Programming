"""
Given an array of integers, return whether or not two numbers sum to a given target, k. 
Note: you may not sum a number with itself. 

Ex: Given the following...
[1, 3, 8, 2], k = 10, return true (8 + 2)
[3, 9, 13, 7], k = 8, return false
[4, 2, 6, 5, 2], k = 4, return true (2 + 2)

"""

def twoSums(arr,k):
    d={}
    for i in range(len(arr)):
        if k-arr[i] in d.keys():
            return True
        d[arr[i]]=i
        # print(d)
    return False

if __name__=="__main__":
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        k=int(input())
        print(twoSums(arr,k))
        
