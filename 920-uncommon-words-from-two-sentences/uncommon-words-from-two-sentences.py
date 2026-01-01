class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_split = s1.split(" ")
        s1_occurences = {}
        for word in s1_split: 
            s1_occurences[word] = s1_occurences.get(word, 0) + 1

        s2_split = s2.split(" ")
        s2_occurences = {}
        for word in s2_split:
            s2_occurences[word] = s2_occurences.get(word, 0) + 1

        uncommon_words = []
        for word in s1_occurences.keys():
            if word not in s2_occurences and s1_occurences[word] == 1:
                uncommon_words.append(word)

        for word in s2_occurences.keys():
            if word not in s1_occurences and s2_occurences[word] == 1:
                uncommon_words.append(word)

        return uncommon_words
