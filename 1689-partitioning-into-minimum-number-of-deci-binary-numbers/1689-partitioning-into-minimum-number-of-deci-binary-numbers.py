class Solution:
    def minPartitions(self, n: str) -> int:
        ans=0
        for i in n:
            ans=max(int(i),ans)
            
            
        return ans
        