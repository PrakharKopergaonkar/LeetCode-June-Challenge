#Question 6 : Coin Change 2

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        m = [[0 for i in range(amount+1)] for j in range(len(coins)+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if(i==0 and j!=0):
                    m[i][j] = 0
                elif(j==0 and i==0):
                    m[i][j] = 1
                elif(j>=coins[i-1]):
                    m[i][j]+=m[i-1][j]+m[i][j-coins[i-1]]
                else:
                    m[i][j]+=m[i-1][j]
        return m[len(coins)][amount]