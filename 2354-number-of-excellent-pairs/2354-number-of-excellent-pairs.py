class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        
        nums = set(nums)
        count1 = sorted([bin(num)[2:].count("1") for num in nums])
        
        res = 0
        n = len(count1)
        print(count1)
        for val in count1:
                remain = k - val
                idx = bisect.bisect_left(count1, remain)
                res += n - idx
                
        return res

        