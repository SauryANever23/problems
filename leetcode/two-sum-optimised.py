class Solutions:
    def twoSum(nums: list[int], target: int) -> list[int]:
        numMap = {} # initializing a hash table
        for i, num in enumerate(nums):
            compliment = target - num 
            if compliment in numMap:
                return [numMap[compliment], i]
            numMap[num] = i 
        return []

print(Solutions.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
            

