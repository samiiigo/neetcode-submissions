class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort() 
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            lookup = set()
            
            for j in range(i + 1, len(nums)):
                req = -(nums[i] + nums[j])
                
                if req in lookup:
                    seen.add((nums[i], req, nums[j]))
                    
                lookup.add(nums[j])
                
        return [list(triplet) for triplet in seen]