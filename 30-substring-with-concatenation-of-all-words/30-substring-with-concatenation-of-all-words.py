class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        d={}
        for i in words:
                d[i]=d.get(i,0)+1
                
        k=len(words[0])
        w_s=0
        lenght=0
        result=[]
        last=0
        while last<len(s)-k+1:
                if s[last:last+k] in d and d[s[last:last+k]]!=0:
                        d[s[last:last+k]]-=1
                        
                        if d[s[last:last+k]]==0:
                                lenght+=1
                                
                        last+=k    
                        if lenght==len(d):
                                result.append(w_s)
                                w_s+=1
                                
                                last=w_s
                                lenght=0
                                d={}
                                for i in words:
                                        d[i]=d.get(i,0)+1
                                        
                                        
                else:
                        w_s+=1
                        last=w_s
                        lenght=0
                        d={}
                        for i in words:
                                d[i]=d.get(i,0)+1
                                
        return result
                                