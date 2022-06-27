class Solution:
    def numOfWays(self, nums: List[int]) -> int:   
        import math
        def combination(n,r):
            return (math.factorial(n) // (math.factorial(r)* math.factorial(n - r)))
        def reorder(nums):
            if len(nums)<=2:
                return 1
            L = []
            R = []
            for i in range(1,len(nums)):
                if nums[i]<nums[0]:
                    L.append(nums[i])
                else:
                    R.append(nums[i])
            return combination(len(L)+len(R),len(L))*reorder(L)*reorder(R)
        return (reorder(nums)-1)% (10**9+7)