# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s=set()
        
        def func(root):
                if not root:
                        return False
                
                if k-root.val in s:
                        return True
                
                
                s.add(root.val)
                
                return (func(root.left) or func(root.right))

        
        
        return func(root)                
                