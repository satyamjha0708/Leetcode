class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d={}
        for i in magazine:
                if i not in d:
                        d[i]=1
                else:
                        d[i]+=1
                        
                        
        for j in ransomNote:
                if j not in d1:
                        d1[j]=1
                else:
                        d1[j]+=1
                
        for k,v in d1.items():
                if k in d and v<=d[k]:
                        continue
                        
                else:
                        return False
                
        else:
                return True
        
        