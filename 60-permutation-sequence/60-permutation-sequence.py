class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l=[i for i in range(1,n+1)]
        fac=1
        for i in range(1,n):
            fac*=i
            
        k=k-1
        
        s=""
        while True:
            s+=str(l[k//fac])
            l.pop(k//fac)
            if len(l)==0:
                break
                
            k=k%fac
            fac=fac//len(l)
            
            
        return s
            