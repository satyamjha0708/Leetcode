# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        def func(root,level,d):
            if not root:
                return 

            q=[]
            q.append([root,level])

            while q:
                ans=q.pop(0)
                l1=ans[1]
                da=ans[0]
                if l1 not in d:
                    d[l1]=[da.val]

                else:
                    d[l1].append(da.val)


                if (da.left):
                    func(da.left,level+1,d)

                if (da.right):
                    func(da.right,level+1,d)
                
            return d
        d={}
        d1=func(root,1,d)   
        ans=[]
        
        for key,values in d.items():
            ans.append(float(sum(values)/len(values)))
            
            
        return ans
        


                
                
        
            
            
        
        
        
        