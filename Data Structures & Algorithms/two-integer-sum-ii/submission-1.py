class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i,num in enumerate(numbers):
            req = target - num
            if req in numbers: 
                return [i+1,numbers.index(req)+1]
        