#Question 13 : Largest Divisible Subset
class Solution:
    def __init__(self):
        self.max_subset = []
        
    def returnsubset(self, nums, temp_list, position, starting_index):
        #if the length of array is only 1
        if(len(nums)==1):
            self.max_subset = [nums[0]]
            return 0
        for i in range(starting_index, len(nums)):
            if(len(temp_list)==0):
                position[i] = i
                self.returnsubset(nums,temp_list + [nums[i]], position, i+1)
            elif(nums[i]%temp_list[len(temp_list)-1]==0 and len(temp_list)+1>position[i]):
                position[i]=len(temp_list)
                if(i==len(nums)-1):
                    if(len(self.max_subset) < len(temp_list)+1):
                        temp_list += [nums[i]]
                else:
                    self.returnsubset(nums,temp_list+[nums[i]], position, i+1)
        
        #if the generated list is greater than the previous max
        if(len(self.max_subset)<len(temp_list)):
            self.max_subset = temp_list
        print(self.max_subset)
                
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        position = []
        nums.sort()
        for i in range(0, len(nums)):
            position.append(-1)
        self.returnsubset(nums, [], position, 0)
        return self.max_subset