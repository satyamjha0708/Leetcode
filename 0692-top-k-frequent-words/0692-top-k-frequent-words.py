class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        
        for i in words:
                if i not in d:d[i]=1
                else:d[i]+=1
                        
        d1=sorted(d, key=lambda item: (-d[item],item))
        return d1[:k]
                        
       
                               
        