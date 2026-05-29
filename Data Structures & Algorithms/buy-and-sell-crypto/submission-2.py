class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, n = 0, 1, len(prices)
        maxprofit = 0

        while l != n-1:

            if l > r: 
                l = r
                r += 1
                continue
            if r==n:
                l += 1
                r = l+1
                continue

            maxprofit = max(maxprofit, prices[r]-prices[l])
            r += 1
        return maxprofit
