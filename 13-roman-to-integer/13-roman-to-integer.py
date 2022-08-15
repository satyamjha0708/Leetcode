class Solution:
    def romanToInt(self, s: str) -> int:
        n=0
        
        for i in range(len(s)):
                if s[i]=='I':
                        n+=1
                        
                elif s[i]=='V':
                        l=s[0:i].count("I")
                        n+=5-2*l*1
                        
                        
                elif s[i]=='X':
                        l=s[0:i].count("I")
                        n+=10-2*l*1
                        
                        
                elif s[i]=='L':
                        l=s[0:i].count("X")
                        n+=50-2*10*l
                        
                        
                elif s[i]=='C':
                        l=s[0:i].count("X")
                        n+=100-2*10*l
                        
                elif s[i]=="D":
                        l=s[0:i].count("C")
                        n+=500-2*l*100
                        
                elif s[i]=="M":
                        l=s[0:i].count("C")
                        n+=1000-2*l*100
                        
                
        return n