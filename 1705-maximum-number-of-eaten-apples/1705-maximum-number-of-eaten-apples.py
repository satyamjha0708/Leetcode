class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap=[]
        index=0
        ans=0
        
        while heap or index<len(apples):
                if index<len(apples):
                        heapq.heappush(heap,[days[index]+index,apples[index]])
                        
                while heap and (heap[0][0]<=index or heap[0][1]==0):
                        heappop(heap)
                
                if heap:
                        ans+=1
                        heap[0][1]-=1
                index+=1
                
        return ans