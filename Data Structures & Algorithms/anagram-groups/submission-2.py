class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i in strs:
            outer=[]
            l=len(i)
            if l not in seen:
                outer.append([i])
                seen[l] = outer
            else:
                found_match = False
                
                for j in seen[l]:
                    if sorted(i) == sorted(j[0]):
                        j.append(i)
                        found_match = True
                        break

                if not found_match:
                    seen[l].append([i])
  
        return [j for i in seen.values() for j in i]