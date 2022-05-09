
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        from itertools import combinations
        d={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        
        l=[]
        for i in digits:
            l.append(d[i])
            
            
        comb=product(*l)
        
        result=[]
        
        for c in comb:
            if not c:
                continue
                
            s=''.join(c)
            
            result.append(s)
            
            
        return result
        
        