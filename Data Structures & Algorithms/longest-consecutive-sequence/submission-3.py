class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        seen = sorted(set(nums))
        print(seen)
        seqno=0
        newlength = {seqno:1}
        i=0
        while (i+1<len(seen)):
            num = seen[i]
            #if seqno not in newlength: newlength[seqno]=1
            if num+1 != seen[i+1]: 
                seqno+=1
                newlength[seqno]=1
            else: 
                newlength[seqno]+=1
            i+=1
        print(newlength)
        return sorted(newlength.values())[-1]