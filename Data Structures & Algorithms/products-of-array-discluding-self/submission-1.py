class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []

        for i in range(len(nums)):
            accmulator=1
            for j in range(len(nums)):
                if j!=i:
                    accmulator*=nums[j]
            prod.append(accmulator)

        return prod