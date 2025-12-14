class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        for i in range(m-n+1):

            substring = haystack[i : i+n]
            if substring == needle:
                return i 
        return -1 
