class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map to store: { value: index }
        seen = {}
        
        for index, num in enumerate(nums):
            # Calculate the number we need to reach the target
            complement = target - num
            
            # If the complement is already in our map, we found the pair!
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, save the current number and its index to the map
            seen[num] = index
