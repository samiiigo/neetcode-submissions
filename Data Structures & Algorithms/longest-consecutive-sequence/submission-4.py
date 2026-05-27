class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        seen = sorted(set(nums))
        seqno=0
        newlength = {seqno:1}
        i=0
        while (i+1<len(seen)):
            if seen[i]+1 != seen[i+1]: 
                seqno+=1
                newlength[seqno]=1
            else: 
                newlength[seqno]+=1
            i+=1
        return sorted(newlength.values())[-1]