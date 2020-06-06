#Question 6 - Queue Reconstruction by Height

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        return_list = []
        for i in range(0, len(people)-1):
            for j in range(i+1, len(people)):
                if(people[i][0] < people[j][0]):
                    people[i], people[j] = people[j], people[i]
                elif(people[i][0] == people[j][0] and people[i][1] > people[j][1]):
                    people[i], people[j] = people[j], people[i]
        for i in range(0, len(people)):
            return_list.insert(people[i][1], people[i])
        return return_list