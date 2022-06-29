# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        global l
        l=[]
        def func(root):
            
            if root:
                func(root.left)
                l.append(root.val)
                func(root.right)
                
           
        func(root)
        l.sort()
        ans=99999
        for i in range(1,len(l)):
            ans=min(ans,l[i]-l[i-1])
            
            
        return ans
            
      
        
        