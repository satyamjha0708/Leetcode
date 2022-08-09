class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def dfs(node,arr,counter=0):
                while arr[node]==-1 and node!=-1:
                        arr[node]=counter
                        
                        
                        dfs(edges[node],arr,counter+1)
                        
                return arr
        
        
        
        res=float('inf')
        arr1=[-1 for i in range(len(edges))]
        ar1=dfs(node1,arr1)
        
        arr2=[-1 for i in range(len(edges))]
        ar2=dfs(node2,arr2)
        answer=-1
        for i in range(len(edges)):
                if ar1[i]!=-1 and ar2[i]!=-1:
                        m=max(ar1[i],ar2[i])
                        
                        
                        if m<res:
                                res=m
                                answer=i
                                
        return answer
        
        
        