class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def func(i):
                return bin(i)[2:].count('1')
        nums=set(nums)
        n=len(nums)
        m=[]
        for i in nums:
                m.append(func(i))
                
        m.sort()
        res=0
        for i in m:
                if i>=k:
                        res+=n
                else:
                        idx=bisect.bisect_left(m,k-i)
                        res+=n-idx
                        
                        
                        
        return res