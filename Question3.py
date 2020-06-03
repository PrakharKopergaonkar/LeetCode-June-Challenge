#Question 3 : Two city scheduling

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        max_people1, max_people2 = 0, 0
        list2 = sorted(costs, key=lambda x: abs(x[0]-x[1]), reverse=True)
        for x in list2:
            if((x[0]<x[1] and max_people1 < int(len(costs)/2)) or (max_people2 >= int(len(costs)/2))):
                min_cost += x[0]
                max_people1+=1
            elif((x[1] < x[0] and max_people2 < int(len(costs)/2)) or (max_people1 >= int(len(costs)/2)-1)):
                min_cost += x[1]
                max_people2 +=  1
        return min_cost