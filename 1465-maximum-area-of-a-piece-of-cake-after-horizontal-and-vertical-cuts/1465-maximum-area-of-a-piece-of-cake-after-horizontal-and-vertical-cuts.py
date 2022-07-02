class Solution:
    def maxArea(self, h: int, w: int, hor: List[int], ver: List[int]) -> int:
        hor.insert(0,0)
        hor.append(h)
        
        ver.insert(0,0)
        ver.append(w)
        
        m1=-1
        m2=-1
        hor.sort()
        ver.sort()
        for i in range(1,len(hor)):
            m1=max(m1,abs(hor[i]-hor[i-1]))
            
            
        for j in range(1,len(ver)):
            m2=max(m2,abs(ver[j]-ver[j-1]))
            
            
            
        return m1*m2%(10**9 + 7)
    