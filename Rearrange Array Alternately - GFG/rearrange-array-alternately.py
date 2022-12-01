#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        arr_t=arr[:]
        k=0
        
        for i in range(n):
            if i%2==0:
                arr[i]=arr_t[n-k-1]
                k+=1
                
                
                
            else:
                arr[i]=arr_t[k-1]
            
        
        

            
            
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends