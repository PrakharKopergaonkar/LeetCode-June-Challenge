# Question 28:  Reconstruct Itinerary
class Solution:
        
    def dfs(self,dest,string,temp_list):
        if(string in dest):
            while(dest[string]):
                a = dest[string].pop()
                self.dfs(dest,a,temp_list)
        temp_list.append(string)
        
                
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dest = dict()
        for i in tickets:
            if(i[0] in dest):
                dest[i[0]].append(i[1])
            
            else:
                dest[i[0]] = []
                dest[i[0]].append(i[1])
        
        for key in dest.keys():
            dest[key].sort(reverse=True)
        
        output_list = []
        self.dfs(dest,'JFK',output_list)
        return output_list[::-1]
        
        
        