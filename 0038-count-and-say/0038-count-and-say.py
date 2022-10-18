class Solution:
    def countAndSay(self, n: int) -> str:
        def func(s):
            s=str(s)
            s = s+"#"
            i = 0
            j = 1
            cnt = 1
            f = ""
            while j < len(s):
                if s[i] == s[j]:
                    cnt += 1
                    i += 1
                    j += 1

                else:
                    f = f+str(cnt)+s[i]

                    print("case2")
                    cnt = 1
                    i += 1
                    j += 1

            return int(f)

        if n==1:
            return str(1)
        x=func(1)
        for i in range(n-2):
            x=func(x)
        return str(x)
 
        