class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=1
        while (i<=len(s)):
            if s[-i]!=' ':
                break
            i += 1
        count=0
        for index in range(i, len(s)+1):
            if s[-index]==' ':
                break
            count+=1
            
        if count==0:
            return 0
        return count