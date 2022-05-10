class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
            res=[]
            def backtrack(i=0,c=1,r=[],s=0):
                if i==k:
                    if s==n:
                        res.append(r[:])
                if i>=k or c>9:
                    return
                r.append(c)
                backtrack(i+1,c+1,r,s+c)
                r.pop()
                backtrack(i,c+1,r,s)

            backtrack()
            return res