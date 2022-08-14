class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        myset=set()
        
        for i in wordList:
                myset.add(i)
                
        if len(wordList)==2:
                if endWord in wordList and beginWord in wordList:
                        return 0
                
        if endWord not in myset:
                return 0
        
        queue=[]
        queue.append(beginWord)
        depth=0
        
        while queue:
                depth+=1
                llen=len(queue)
                
                for _ in range(llen):
                        x=queue.pop(0)
                        
                        for i in range(len(x)):
                                y=list(x)
                                for j in range(ord('a'),ord('z')+1):
                                        y[i]=chr(j)
                                        
                                        if ''.join(y)==''.join(x):
                                                continue
                                                
                                        if ''.join(y)==endWord:
                                                return depth+1
                                        
                                        if ''.join(y) in myset:
                                                queue.append(''.join(y))
                                                myset.remove(''.join(y))
                                                
        return 0
                                                
                                                
                
                                
                                
                                
                                
                        
        