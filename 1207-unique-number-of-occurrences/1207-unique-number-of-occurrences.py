class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
                if i not in d:
                        d[i]=arr.count(i)
           
        s=set()
                        
        for i,j in d.items():
                if j not in s:
                        s.add(j)
                        
                else:
                        return False
                
                
        return True
