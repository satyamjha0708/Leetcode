class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def pali(s):
            return s==s[::-1]
        def func(index,s,temp,ans,n):
            if index==n:
                ans.append(temp[:])
                
                return 
        
            for i in range(index,len(s)):
                if pali(s[index:i+1]):
                    temp.append(s[index:i+1])
                    func(i+1,s,temp,ans,n)
                    temp.pop()
                    
                    
        ans=[]    
        func(0,s,[],ans,len(s))
        return ans
            
            
        