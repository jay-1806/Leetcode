class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        if k > n:
            return False

        def idx(c): return ord(c) - ord('a')

        need = [0]*26
        win  = [0]*26
        for ch in s1:
            need[idx(ch)] += 1
        for ch in s2[:k]:
            win[idx(ch)] += 1

        matches = sum(1 for i in range(26) if need[i] == win[i])
        if matches == 26:
            return True

        for i in range(k, n):
            add_i = idx(s2[i])
            rem_i = idx(s2[i - k])

            # add right char
            old = win[add_i]
            win[add_i] += 1
            if win[add_i] == need[add_i]:
                matches += 1
            elif old == need[add_i]:
                matches -= 1

            # remove left char
            old = win[rem_i]
            win[rem_i] -= 1
            if win[rem_i] == need[rem_i]:
                matches += 1
            elif old == need[rem_i]:
                matches -= 1

            if matches == 26:
                return True
        return False
