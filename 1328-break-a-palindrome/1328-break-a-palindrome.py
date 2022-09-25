class Solution:
    def breakPalindrome(self, pal):
        n = len(pal)
        for i in range(n//2):
            if pal[i] != "a": return pal[:i] + "a" + pal[i+1:]
        return pal[:-1] + "b" if n > 1 else ""
        