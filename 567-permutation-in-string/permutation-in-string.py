class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        l = 0
        s2_count = {}

        for r in range(len(s2)):
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1

            while r - l + 1 > len(s1):
                s2_count[s2[l]] -= 1
                if s2_count[s2[l]] == 0:
                    del s2_count[s2[l]]
                l += 1

            if r - l + 1 == len(s1):
                if s2_count == s1_count:
                    return True
        return False

        