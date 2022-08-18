from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d=Counter(arr)
        d1={k: v for k, v in sorted(d.items(), key=lambda item: item[1],reverse=True)}
        cnt=0
        ans=0
        
        for k,v in d1.items():
                ans+=v
                                   
                        
                cnt+=1
                if ans>=len(arr)//2:
                        break
     

                
        return cnt