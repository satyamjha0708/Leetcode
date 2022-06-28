# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def func(root,s):
            if root==None:
                return False
            
            if root.left==None and root.right==None:
             
                if root.val==s:
                    return True
                
                else:
                    return False

            
            
            
            

            return func(root.left,s-root.val) or func(root.right,s-root.val)
                
        
        
        
        return func(root,targetSum)
            
                
                
        
        