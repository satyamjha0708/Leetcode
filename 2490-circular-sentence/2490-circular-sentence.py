class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        l=sentence.split(' ')
        print(l)
        
        if len(l)==1:
                return l[0][0]==l[-1][-1]
        
        if len(l)==2:
                if l[0][0]==l[-1][-1] and l[0][-1]==l[-1][0]:
                        return True
                
                
                else:
                        return False
                
        
        for i in range(len(l)-1):
                if i==0 :
                        if l[i][0]!=l[-1][-1]:
                                return False
                        
                        
                        
                elif l[i][-1]!=l[i+1][0]:
                        return False
                
                
                
        else:
                return True
        
        