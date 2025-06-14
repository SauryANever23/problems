class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        sol = []
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if (num + nums[j]) == target:
                    sol.append(nums.index(num))
                    sol.append(nums.index(nums[j]))
                    break
            break 
        print(sol)
        
Solution.twoSum([1,3,4,5,6], 5) 


