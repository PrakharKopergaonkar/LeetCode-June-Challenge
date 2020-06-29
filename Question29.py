#  Question 29: Unique Paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        output_list = [[0 for i in range(m)] for j in range(n)]
        
        output_list[n-1][m-1] = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if(i==n-1 and j==m-1):
                    continue
                else:
                    sum1 = 0
                    if(i+1<=n-1):
                        sum1+=output_list[i+1][j]
                    if(j+1<=m-1):
                        sum1+=output_list[i][j+1]
                    output_list[i][j] = sum1
        return output_list[0][0]