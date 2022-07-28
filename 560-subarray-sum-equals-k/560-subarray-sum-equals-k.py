class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        s=0
        cnt=0
        d[0]=1
        for i in range(len(nums)):
            s+=nums[i]
            
            if s-k in d:
                cnt+=d[s-k]
                
                
            if s not in d:
                d[s]=1
                
                
            else:
                d[s]+=1
                
                
        return cnt