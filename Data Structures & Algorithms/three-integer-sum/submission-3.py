class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort() 
        
        for i in range(len(nums)):
            lis = set()

            for j in range(i + 1, len(nums)):
                req = -(nums[i] + nums[j])

                if req in nums[j + 1:]:
                    seen.add((nums[i], req, nums[j]))
                
        return list(seen)


        