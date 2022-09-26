class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nums = list(zip(heights, names))
        ans = []
        nums.sort(reverse=True)
        for x, y in nums:
            ans.append(y)
        return ans