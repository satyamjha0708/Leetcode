#User function Template for python3

class Solution:
    ans_list = []
    
    def wordBreak(self, n, words, s):
        self.ans_list = []
        self.solve(words, s, "")
        return self.ans_list
        
    def solve(self, words, s, result_string):
        for word in words:
            # init
            result_string_copy = result_string
            
            # final word
            if s == word:
                result_string_copy = result_string_copy + " " + word
                self.ans_list.append(result_string_copy.strip())
            
            # search next word and continue
            if s.startswith(word):
                result_string_copy = result_string_copy + " " + word
                self.solve(words, s[len(word):], result_string_copy)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dict = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dict, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends