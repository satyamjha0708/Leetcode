class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def solve(s,words):
            found = {}
            for word in words:
                found[word] = found.get(word,0)+1
            k = len(words[0])
            ws = 0
            last = 0
            result = []
            length = 0
            while last<len(s)-k+1:
                if s[last:last+k] in found and found[s[last:last+k]]!=0:
                    # print(s[last:last+k],last,ws,found)
                    found[s[last:k+last]] -= 1 
                    if found[s[last:k+last]] == 0:
                        length += 1 
                    last = last + k 
                    if length == len(found):
                        result.append(ws)
                        ws += 1 
                        last = ws
                        length = 0
                        found = {}
                        for word in words:
                            found[word] = found.get(word,0)+ 1
                else:
                    # print(found,last,ws)
                    ws += 1 
                    last = ws
                    length = 0
                    found = {}
                    for word in words:
                        found[word] = found.get(word,0)+1
            return result
        return solve(s,words)