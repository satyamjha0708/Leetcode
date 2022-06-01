class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=nums[0]
        d=nums[0]
        
        
        for i in range(1,len(nums)):
            c=max(nums[i],c+nums[i])
            
            d=max(d,c)
            
            
        return d
            