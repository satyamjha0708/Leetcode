# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        global arr
        arr=[]
        
        def func(root):
            if root:
                func(root.left)
                arr.append(root.val)
                func(root.right)
                
        func(root)        
        for i in range(1,len(arr)):
            if arr[i-1]!=arr[i]:
                return False
            
            
        return True
                