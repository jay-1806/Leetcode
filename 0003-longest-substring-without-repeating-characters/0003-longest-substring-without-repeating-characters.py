class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l , res = 0 , 0 
        mp = {}

        #zxyz

        for r in range(n):
            current_char = s[r]

            if current_char in mp:
                l = max(mp[current_char] + 1 , l)
            
            mp[current_char] = r
            res = max(res, r-l+1)
        return res