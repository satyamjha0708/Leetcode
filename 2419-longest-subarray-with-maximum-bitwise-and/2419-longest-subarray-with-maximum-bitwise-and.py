class Solution:
    def longestSubarray(self, arr: List[int]) -> int:
        x=max(arr)
        ans, temp = 1, 1
        for i in range(1, len(arr)):
                if arr[i]==x and arr[i] == arr[i - 1]:
                        temp = temp + 1
                else:
                        ans = max(ans, temp)
                        temp = 1
                        
                ans = max(ans, temp)
                
        return ans
        