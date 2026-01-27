class Solution:
    def findValidPair(self, s: str) -> str:
        number_frequency = {}
        for n in s:
            number_frequency[n] = number_frequency.get(n, 0) + 1

        valid_pair = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                continue
            else: 
                if number_frequency[s[i]] == int(s[i]) and number_frequency[s[i+1]] == int(s[i+1]):
                    valid_pair.append(s[i])
                    valid_pair.append(s[i+1])
                    break

        return "".join(valid_pair)