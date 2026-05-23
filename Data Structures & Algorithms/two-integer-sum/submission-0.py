class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            oth = target-num
            if oth in seen:return [seen[oth],i]
            seen[num]=i
