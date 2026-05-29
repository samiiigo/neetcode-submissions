class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ar = []
        size = len(heights)
        for i in range(size):
            for j in range(i+1,size):
                
                ar.append((j-i)*min(heights[i],heights[j]))

        return(max(ar))
