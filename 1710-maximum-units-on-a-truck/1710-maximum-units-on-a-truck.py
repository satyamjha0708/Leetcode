class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x: x[1],reverse=True)
        ans=0
        total=0
        i=0
        while  i<len(boxTypes) and ans+boxTypes[i][0]<truckSize:
            ans+=boxTypes[i][0]
            total+=boxTypes[i][0]*boxTypes[i][1]
            i+=1

        
        if ans!=truckSize and i<len(boxTypes): 
            
            total+=(truckSize-ans)*(boxTypes[i][1])
        
        return total