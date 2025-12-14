class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmp = {}

        for c in magazine:
            hashmp[c] = 1 + hashmp.get(c,0)
        
        for c in ransomNote:
            if c not in hashmp or hashmp[c] <= 0:
                return False
            hashmp[c] -= 1
        
        return True

