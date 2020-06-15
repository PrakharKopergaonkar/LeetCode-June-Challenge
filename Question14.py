# Question 14 : Cheapest Flights Within K Stops
import sys
class Solution:
    def __init__(self):
        self.flights = None
        self.cost = sys.maxsize
    def findroute(self, src, dst, k, curr_cost, visited):
        print(src, dst, curr_cost)
        while(True):
            if(k<0):
                break
            
            elif(self.cost < curr_cost):
                return True
                break
            
            elif(src == dst):
                if(curr_cost < self.cost):
                    self.cost = curr_cost
                    return True
                break
            
            else:
                possible_paths = sorted([m for m in self.flights if(m[0]==src)], key = lambda x: x[2])
                for i in possible_paths:
                    visitedtemp = visited.copy()
                    if(visitedtemp[i[1]]==False and curr_cost+i[2]<self.cost):
                        visitedtemp[i[1]]=True
                        a = self.findroute(i[1],dst,k-1,curr_cost+i[2], visitedtemp)
                        if(a==True):
                            break
                break
                
                
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        visited = []
        for i in range(n):
            visited.append(False)
        visited[src] = True
        self.flights = flights
        self.findroute(src, dst, K+1, 0, visited)
        if(self.cost == sys.maxsize):
            return -1
        return self.cost
        