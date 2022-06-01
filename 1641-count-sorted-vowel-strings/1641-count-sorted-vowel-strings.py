class Solution:
    def countVowelStrings(self, n: int) -> int:
        l=[1]*5
        
        
        for i in range(1,n):
            for i in range(3,-1,-1):
                l[i]+=l[i+1]
                
                
        return sum(l)