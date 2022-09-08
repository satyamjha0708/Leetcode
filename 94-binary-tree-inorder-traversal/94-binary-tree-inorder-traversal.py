# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global ans
        ans=[]
        def func(root):
                if root:
                        func(root.left)
                        ans.append(root.val)
                        func(root.right)
                        
        func(root)                
        return ans