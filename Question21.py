# Question 21 : Dungeon Game
import sys
class Solution:
    def generatehealth(self,dungeon, current_row, current_col,key):
        if(current_row>=len(dungeon) or current_col >= len(dungeon[0])):
            return sys.maxsize
        else:
            string = str(current_row)+'p'+str(current_col)
            if(string in key):
                return key[string]
            health = min(self.generatehealth(dungeon,current_row+1,current_col,key), self.generatehealth(dungeon, current_row, current_col+1,key))
            if(health == sys.maxsize):
                health = 1
            res = 0
            if(health - dungeon[current_row][current_col]>0):
                res = health - dungeon[current_row][current_col]
            
            else:
                res = 1
            key[str(current_row)+'p'+str(current_col)] = res
            return res
            
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        current_row = 0
        current_col = 0
        key = dict()
        result = self.generatehealth(dungeon,current_row,current_col,key)
        return result