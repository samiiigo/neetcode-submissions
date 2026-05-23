class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_nums={}
        for i in nums:
            if i in dict_nums:return True
            dict_nums[i]=1
                
        

        return False