# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        global l
        l=[]
        
        
        def fun(root):
            if root:
                l.append(root)
                fun(root.left)
                fun(root.right)
            
            
            
        fun(root)
        
        for i in range(len(l)-1):
            l[i].right=l[i+1]
            l[i].left=None
            
            
    