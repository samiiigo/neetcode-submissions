class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ar = []
        for i, height1 in enumerate(heights):
            for j, height2 in enumerate(heights):
                ar.append((j-i)*min(height1,height2))
        return(max(ar))

