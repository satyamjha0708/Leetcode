#User function Template for python3
class Solution:

    def sieve(self):

        l=[0]*10000001

        b=[] 

        k=2

        while k*k<=1000000000000:

            if l[k]==0:

                b.append(k*k)

                j=k*k 

                for i in range(j,10000001,k):

                   l[i]=1 

                   pass

            k+=1 

        return b

    def threeDivisors(self, query, q):

        l=self.sieve()

        li=[]

        for j in query:

            c=0

            for i in l:

                if i<=j:

                    c+=1 

                else:

                    break 

            li.append(c)

        return li


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		q = int(input())
		query = []
		for _ in range(q):
			query.append(int(input()))
		
		ob = Solution()
		ans = ob.threeDivisors(query,q)
		for a in ans:
			print(a)

# } Driver Code Ends