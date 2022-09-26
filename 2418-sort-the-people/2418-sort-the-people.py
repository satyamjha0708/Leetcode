class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(heights)):
                d[heights[i]]=names[i]
                
        
        ans=[]
        heights.sort(reverse=True)
        
        for i in heights:
                ans.append(d[i])
                
                
        return ans