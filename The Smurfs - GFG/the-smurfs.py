#User function Template for python3

class Solution:
    def minFind(self, n, a):
        r=0
        g=0
        b=0
        for i in a:
            if i=='R':
                r+=1
                
            elif i=='B':
                b+=1
                
            else:
                g+=1
                
                
                
        if r==n or g==n or b==n:
            return n
            
        
        if (r%2==0 and b%2==0 and g%2==0) or (r%2==1 and g%2==1 and b%2==1):
            return 2
            
        else:
            return 1
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        
        ob = Solution()
        print(ob.minFind(n, a))
# } Driver Code Ends