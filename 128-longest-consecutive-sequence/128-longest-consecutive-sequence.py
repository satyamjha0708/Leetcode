class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        if len(nums)==0:
            return 0
            
        for i in nums:
            s.add(i)
        ans=0    

        curr=1
        curnum=0
        for i in nums:
            if (i-1) not in s :
                curr=1
                currnum=i
                
                
                while currnum+1 in s:
                    curr+=1
                    currnum+=1
                    
                ans=max(curr,ans)
                
                
                
        return ans