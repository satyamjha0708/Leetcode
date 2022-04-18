# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        def func(root):
            if root:
                func(root.left)
                l.append(root.val)
                func(root.right)
                
        func(root)        
        if k>len(l):
            return -1
        else:
            return l[k-1]
        