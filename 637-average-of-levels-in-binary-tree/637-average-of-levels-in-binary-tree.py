# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans=[]
        queue=[root]
        m=[]
        while queue:
                
                size=len(queue)
                l=[]
                
                for i in range(size):
                        x=queue.pop(0)
                        if x.left:
                                queue.append(x.left)
                                
                        if x.right:
                                queue.append(x.right)
                                
                        l.append(x.val)
                        
                m.append(float(sum(l)/len(l)))
                
                
        return m

                
                
        
            
            
        
        
        
        