# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(root,l,arr):
                if root==None:
                        return False
                
                arr.append(root)
                
                if root.val==l:
                        return True
                
                
                if func(root.left,l,arr) or func(root.right,l,arr):
                        return True
                
                
                arr.pop()
                return False
        
        arr=[]
        arr1=[]
        func(root,p.val,arr)
        func(root,q.val,arr1)
        
        
        for i in range(len(arr)-1,-1,-1):
                if arr[i] in arr1:
                        return arr[i]
        
        
        
        
                
                
                
        