class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxleft=nums[0]
        maxright=nums[0]
        
        prod=1
        
        zero=False
        
        for i in nums:
            prod*=i
            
            if i==0:
                prod=1
                zero=True
                
                continue
                
            maxleft=max(maxleft,prod)
            
            
        prod=1
        for j in nums[::-1]:
            prod*=j
            
            if j==0:
                prod=1
                zero=True
                
                continue
                
                
            maxright=max(maxright,prod)
            
            
            
        if zero:
            return max(max(maxleft,maxright),0)
        
        else:
            return max(maxleft,maxright)
                