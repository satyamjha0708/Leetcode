class Solution:
    def minimumSum(self, num: int) -> int:
        l=[]
        while num:
                l.append(num%10)
                num=num//10
                
                
        l.sort()
        
        return (((l[0]*10)+l[-1])+(l[1]*10+l[-2]))
                
                
                
                