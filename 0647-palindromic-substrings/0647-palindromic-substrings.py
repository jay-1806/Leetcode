class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                sub_str = s[i:j+1]
                if sub_str == sub_str[::-1]:
                    count += 1
                
        return count
        
