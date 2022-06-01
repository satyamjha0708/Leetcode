class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s1=set(nums)
        
        if len(s1)!=len(nums):
            return True
        else:
            return False
        
        
        