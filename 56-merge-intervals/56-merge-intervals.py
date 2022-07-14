class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort()
        ans=[]
        for i in range(len(arr)):
            start=arr[i][0]
            end=arr[i][1]
        
            if len(ans)!=0:
                if start<=ans[-1][1]:
                    continue
                
                
                
            for j in range(i+1,len(arr)):
                if arr[j][0]<=end:
                    end=max(end,arr[j][1])
                    
                    
                    
            
            ans.append([start,end])
            
            
        
        
        return ans