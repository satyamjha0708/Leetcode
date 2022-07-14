class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort()
        ans=[]
        
        
        for i in range(len(arr)):
            if len(ans)==0 or ans[-1][1]<arr[i][0]:
                ans.append([arr[i][0],arr[i][1]])
                
                
            else:
                ans[-1][1]=max(arr[i][1],ans[-1][1])
                
                
                
                
        return ans