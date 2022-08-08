class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]]=[]      
                
      
                
        ans=9999        
        for x,y in d.items():
            if len(y)>0:
                ans=min(ans,y[0])
                
                
                
        return s[ans]