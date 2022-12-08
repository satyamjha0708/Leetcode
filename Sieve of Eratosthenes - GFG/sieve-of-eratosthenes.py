#User function Template for python3

class Solution:
    def sieveOfEratosthenes(self, N):
        arr=[True for i in range(N+1)]
        p=2
        
        while p*p<=N:
            if arr[p]==True:
                for i in range(p*p,N+1,p):
                    arr[i]=False

                    
                    
            p+=1
                    
        ans=[]
        for i in range(2,N+1):
            if arr[i]:
                ans.append(i)
                
                
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends