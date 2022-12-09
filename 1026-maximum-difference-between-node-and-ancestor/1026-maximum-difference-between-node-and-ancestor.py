# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.Max=0
        def func(root,mini,maxi):
                if not root:
                        return
                
                
                self.Max = max(self.Max, abs(root.val-mini), abs(root.val-maxi))
        
                maxi=max(maxi,root.val)
                mini=min(mini,root.val)
                
                
                func(root.left,mini,maxi)
                func(root.right,mini,maxi)
        
        

        func(root,root.val,root.val)
        return self.Max
