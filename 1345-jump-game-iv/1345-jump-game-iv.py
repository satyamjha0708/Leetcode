class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d={}
        n=len(arr)
        for i in range(len(arr)):
                if arr[i] in d:
                        d[arr[i]].append(i)
                        
                        
                else:
                        d[arr[i]]=[i]
                        
        
        visited=[False]*len(arr)
        visited[0]=True
        print(d)
        queue=[0]
        step=0
        while queue:
                for _ in range(len(queue)):
                        i=queue.pop(0)
                        if i==n-1:
                                return step
                        nxt=d[arr[i]]
                        nxt.append(i-1)
                        nxt.append(i+1)

                        for j in nxt:
                                if j>=0 and j<n and visited[j]==False:
                                        visited[j]=True
                                        queue.append(j)
                        d[arr[i]].clear()
                step+=1
                
                
        
                
                
                
        
        
        
        