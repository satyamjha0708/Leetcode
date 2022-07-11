class Solution:
    def fillCups(self, amount: List[int]) -> int:
        import heapq
        h=[]
        for i in amount:
            if i>0:
                heappush(h,-i)
                
        result=0
        while len(h)>1:
            first=-heappop(h)
            second=-heappop(h)
            
            
            result+=1
            first-=1
            second-=1
            
            
            if first>0:
                heappush(h,-(first))
                
            if second>0:
                heappush(h,-(second))
                
            
            
        if h:
            return result-h[0]
        
        else:
            return result
            
            
            