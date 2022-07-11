# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        
        ans=[]
        queue=[]
        queue.append(root)
        
        
        while queue:
            lastnode=None
            for _ in range(len(queue)):
                curr=queue.pop(0)
                lastnode=curr
                
                if curr.left:
                    queue.append(curr.left)
                    
                if curr.right:
                    queue.append(curr.right)
                    
                    
            ans.append(lastnode.val)
            
            
        return ans
    
            
        
        
        