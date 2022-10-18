class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def func(n):
                number=0
                while n:
                        d=n%10
                        number=number*10+d
                        n=n//10
                        
                return number
        d={}
        for i in nums:
                if i not in d:d[i]=1
                        
                else:d[i]+=1
                        
                        
                        
        for i in nums:
                if func(i) not in d:d[func(i)]=1
                
                else:d[i]+=1
        return len(d)
                        
        