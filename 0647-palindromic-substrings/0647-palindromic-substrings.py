class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i,n):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    res += 1
        return res

