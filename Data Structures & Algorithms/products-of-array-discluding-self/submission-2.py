class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []

        for i in nums:
            num=list(nums)
            accmulator=1
            num.remove(i)
            for j in num:
                accmulator*=j
            prod.append(accmulator)

        return prod