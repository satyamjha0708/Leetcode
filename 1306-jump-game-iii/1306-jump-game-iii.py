class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visit=[False]*len(arr)
        
        def help(arr,i):
                if i>=len(arr) or i<0:
                        return False
                
                if arr[i]==0:
                        return True
                
                if visit[i]:
                        return False
                
                visit[i]=True
                
                x=help(arr,i+arr[i])
                y=help(arr,i-arr[i])
                
                return x or y
        
        
        
        return help(arr,start)