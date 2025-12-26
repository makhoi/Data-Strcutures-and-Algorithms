class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # create a ranking system for each character of each string in the array 
        rank_record = {}

        for vote in votes: 
            for i, char in enumerate(vote):
                if char not in rank_record:
                    rank_record[char] = [0] * len(vote)
                # for each character in the string, we add 1 to position theyre ranked
                rank_record[char][i] += 1
        # Sort rank_record.keys() based on their ranking values in dictionary, in descending order in case of equal votes, we alphabetically order the keys first using .sort()
        voted_names = sorted(rank_record.keys()) # this is for final tie-breaker: alphabetical order
        
        # Join elements in the sorted list into a string
        return "".join(sorted(voted_names, key=lambda x: rank_record[x], reverse=True))
