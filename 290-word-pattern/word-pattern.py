class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_s = s.split()

        if len(pattern) != len(new_s):
            return False

        dict1 = {}

        for index in range(len(pattern)):
            if pattern[index] not in dict1:
                dict1[pattern[index]] = new_s[index]
            else:
                if dict1[pattern[index]] != new_s[index]:
                    return False
        
        dict2 = {}

        for index in range(len(new_s)):
            if new_s[index] not in dict2:
                dict2[new_s[index]] = pattern[index]
            else:
                if dict2[new_s[index]] != pattern[index]:
                    return False
        return True