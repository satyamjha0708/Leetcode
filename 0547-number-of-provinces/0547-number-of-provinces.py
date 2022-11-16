class Solution:
    def findCircleNum(self, prov: List[List[int]]) -> int:
        
        
        def dfs(i,graph,visited):
                
                
                for j in graph[i]:
                        if visited[j]==False:
                                visited[j]=True
                                dfs(j,graph,visited)
                                
        
        
        
        graph=collections.defaultdict(list)
        
        
        
        for i in range(len(prov)):
                for j in range(i+1,len(prov)):
                        if prov[i][j]==1:
                                graph[i].append(j)
                                graph[j].append(i)

                        
        
        ans=0
        
        visited=[False]*len(prov)
        for i in range(len(prov)):
                if visited[i]==False:
                        ans+=1
                        visited[i]=True
                        dfs(i,graph,visited)
                        
                        
        return ans