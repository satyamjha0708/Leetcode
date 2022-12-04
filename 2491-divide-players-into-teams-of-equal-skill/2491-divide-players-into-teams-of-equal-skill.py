class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        ans=0
        key=skill[-1]+skill[0]
        while i<j:
                
                if key!=(skill[i]+skill[j]):
                        return -1
                
                
                ans+=skill[i]*skill[j]
                i+=1
                
                j-=1
                
                
        return ans
                
                
                
                
                
        