# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global flag
        flag=True
        
        def func(root):
                if root==None:
                        return 0
                
                l=func(root.left)
                r=func(root.right)
                
                if l==-1 or r==-1 or abs(l-r)>1:
                        return -1
                        
                
                return 1+max(l,r)
        
        return func(root)!=-1
        
        