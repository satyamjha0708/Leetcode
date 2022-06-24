# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    import queue
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q_clone=deque([cloned])
        q=deque([original])
        
        while q:
            q_ori=q.popleft()
            q_clo=q_clone.popleft()
            
            if q_ori==target:
                return q_clo
            
            if q_ori.left:
                q.append(q_ori.left)
                q_clone.append(q_clo.left)
                
            if q_ori.right:
                q.append(q_ori.right)
                q_clone.append(q_clo.right)
                
                
                

                
            
        
        
        
    
        