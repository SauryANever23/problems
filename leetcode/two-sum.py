import random
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol_in = []
        for i, num in enumerate(nums):
            ran = random.randint(0, len(nums)-1) 
            if (num + nums[i+ran]) == target:
                sol_in.append(num)
                sol_in.append(num)
        print(sol_in)

        
        
