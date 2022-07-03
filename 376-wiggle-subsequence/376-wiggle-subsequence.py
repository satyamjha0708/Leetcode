class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        i=1
        j=1
        for k in range(1,len(nums)):
            if nums[k]>nums[k-1]:
                j=i+1
                
                
            elif nums[k]<nums[k-1]:
                i=j+1
                
                
        return max(i,j)