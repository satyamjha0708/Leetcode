class Solution:
    def canFinish(self, numCourses: int, nums: List[List[int]]) -> bool:
        
        def func1(i,d,visited,dfsvisited):
            visited[i]=True
            dfsvisited[i]=True
            
            for j in d[i]:
                if visited[j]!=True:
                    if func1(j,d,visited,dfsvisited):
                        return True
                    
                    
                if dfsvisited[j]==True:
                    return True
                
            dfsvisited[i]=False
            return False
            
        
        
        def func(d,V):
            visited=[False]*(V+1)
            dfsvisited=[False]*(V+1)
            for i in range(V):
                if visited[i]!=True:
                    if func1(i,d,visited,dfsvisited):
                        return True
                
            else:
                return False
        
        d={}
        
        for i in nums:
            if i[0] not in d:
                d[i[0]]=[]
                
            d[i[0]].append(i[1])
            
            
        for i in range(numCourses):
            if i not in d:
                d[i]=[]
            
        print(d)
        return not func(d,numCourses)
            
            
        