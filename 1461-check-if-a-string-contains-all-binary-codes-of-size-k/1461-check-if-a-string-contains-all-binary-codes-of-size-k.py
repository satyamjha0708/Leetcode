class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        s1=set()

        for i in range(0,len(s)):
            if len(s[i:i+k])==k:
                s1.add(s[i:i+k])

          
        
        if len(s1)==2**k:
            return True
        
        else:
            return False
        