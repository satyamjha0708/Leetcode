class Solution:
    def climbStairs(self, n: int) -> int:
        global dp
        dp=[-1]*(n+1)
        def func(n):
                if n==0:
                        dp[n]=1
                        return dp[n]
                if n==1:
                        dp[n]=1
                        return dp[n]
                
                if dp[n]!=-1:
                        return dp[n]
                l=func(n-1)
                r=func(n-2)
                
                dp[n]=l+r
                return dp[n]
        
        
        func(n)
        return dp[-1]