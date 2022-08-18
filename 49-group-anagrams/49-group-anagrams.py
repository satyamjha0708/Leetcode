class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}

        for i in strs:
                l=''.join(sorted(list(i)))
                if l not in d:
                        d[l]=[i]
                        
                else:
                        d[l].append(i)
                        
                        
        return list(d.values())

