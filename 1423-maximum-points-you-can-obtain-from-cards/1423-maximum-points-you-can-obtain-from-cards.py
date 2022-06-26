class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s=sum(cardPoints[:k])
        ans=s
        for i in range(1,k+1):
            s=s+cardPoints[-i]-cardPoints[k-i]
            ans=max(s,ans)
        
        return ans
        