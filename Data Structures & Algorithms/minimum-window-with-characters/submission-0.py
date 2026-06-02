class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Helper to check if current substring satisfies the requirement
        def is_valid(sub, t_map):
            for char in t_map:
                if sub.count(char) < t_map[char]:
                    return False
            return True

        # Pre-calculate frequency map for t
        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1
            
        n1 = len(s)
        
        # Iterate through possible lengths, starting from shortest possible
        for length in range(len(t), n1 + 1):
            # Move the window across the string
            for l in range(n1 - length + 1):
                r = l + length
                sub = s[l:r]
                
                # Check if this specific window is valid
                if is_valid(sub, t_map):
                    return sub
                    
        return ""