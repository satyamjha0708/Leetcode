class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        counts1 = Counter(nums1)
        counts2 = Counter(nums2)
                
        for k in counts1.keys():
            if k in counts2:
                for i in range(min(counts1[k], counts2[k])):
                    result.append(k)
                
        return result