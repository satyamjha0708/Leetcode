class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=1 
        while i<n:
                i=i*4
                
                print(i)
                
        if i==n:
                return True
        
        else:
                return False