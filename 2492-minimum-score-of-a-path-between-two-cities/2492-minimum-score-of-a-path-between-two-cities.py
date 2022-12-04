class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d=defaultdict(list)
        
        
        for x,y,c in roads:
                d[x].append([y,c])
                d[y].append([x,c])
                
                
                
        visit=set()
        res=[9999999999]
        
        
        def  dfs(node,prev):
                visit.add((prev,node))
                
                for i,cost in d[node]:
                        if (i,node) in visit or (node,i) in visit:
                                continue
                                
                                
                        res[0]=min(res[0],cost)
                        
                        dfs(i,node)
        
        
        
        
        dfs(1,None)
        
        
        return res[0]
        