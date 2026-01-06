class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        def expand_around_center(s,left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right-left-1
            
        start = 0 
        end = 0

        for i in range(len(s)):
            odd = expand_around_center(s, i, i)
            even = expand_around_center(s, i, i+1)

            len_max = max(odd,even)

            if len_max > end - start:
                start = i - (len_max - 1) // 2
                end = i + len_max // 2

        return s[start:end+1]

        
        