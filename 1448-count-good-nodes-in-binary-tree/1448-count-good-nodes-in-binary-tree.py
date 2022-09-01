# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

    
        def func(root,m,ans):
                if root==None :
                        return
                if root.val>=m:
                        ans[0]+=1
                        m=root.val
                        
                func(root.left,m,ans)
                func(root.right,m,ans)
        ans=[0]        
        func(root,-float('inf'),ans)
        return ans[0]
                
                
                
                        