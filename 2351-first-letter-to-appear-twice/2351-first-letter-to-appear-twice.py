class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s1=set()
        for i in s:
                if i in s1:
                        return i
                s1.add(i)
                
                
               
              