class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i=1
        while i<n:
                i=i*3
                
        if i==n:
                return True
        
        else:
                return False
        