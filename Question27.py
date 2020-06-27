#Questino 27: Perfect Squares

import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxsize for i in range(0,n+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            j = 1
            while(j*j<=n):
                dp[i] = min(dp[i],1+dp[i-(j*j)])
                j+=1
        
        return dp[n]