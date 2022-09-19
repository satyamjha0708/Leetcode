# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(root,p,q):
                if root==None or root==q or root==p:
                        return root
                
                l=func(root.left,p,q)
                r=func(root.right,p,q)
                
                if l==None:
                        return r
                if r==None:
                        return l
                
                
                else:
                        return root
                
                
        return func(root,p,q)
        
        
        
                
                
                
        