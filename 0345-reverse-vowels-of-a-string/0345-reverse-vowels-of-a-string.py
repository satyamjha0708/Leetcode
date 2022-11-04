class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        
        j=len(s)-1
        
        s=list(s)
        
        s1=['a','e','i','o','u','A','E','I','O','U']
        
        while i<j:
                if  s[i] in s1 and s[j] in s1:
                        s[i],s[j]=s[j],s[i]
                        i+=1
                        j-=1
                        
                        
                elif s[i] in s1 and s[j] not in s1:
                        j-=1
                        
                        
                elif s[i] not in s1 and s[j] in s1:
                        i+=1
                        
                        
                else:
                        i+=1
                        j-=1
                        
                        
        return "".join(s)
                        