class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            # If the current number is greater than 0, we can't sum to 0 anymore
            if nums[i] > 0:
                break
                
            # Skip duplicate numbers for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Use two pointers for the remaining array
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate numbers for the second element to avoid duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res