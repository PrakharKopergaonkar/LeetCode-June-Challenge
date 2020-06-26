# Question 17 : Surrounded Regions
class Solution:
    def DFS(self, board, row, column):
        if(row<0 or row>=len(board) or column<0 or column>=len(board[0]) or board[row][column]!="O"):
            return
        board[row][column] = "#"
        self.DFS(board, row+1, column)
        self.DFS(board, row-1, column)
        self.DFS(board, row, column+1)
        self.DFS(board, row, column-1)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if(len(board)==0) : return 
        for i in range(0, len(board[0])):   
            if(board[0][i]=="O"):
                self.DFS(board, 0, i)
            
            if(board[len(board)-1][i]=="O"):
                self.DFS(board,len(board)-1,i)
        
        for i in range(0, len(board)):
            if(board[i][0]=="O"):
                self.DFS(board, i, 0)
            
            if(board[i][len(board[0])-1]=="O"):
                self.DFS(board,i, len(board[0])-1)
            
        
        for i in range(0,len(board)):
            for j in range(0, len(board[0])):
                if(board[i][j]=="#"):
                    board[i][j]="O"
                
                else:
                    board[i][j]="X"
      