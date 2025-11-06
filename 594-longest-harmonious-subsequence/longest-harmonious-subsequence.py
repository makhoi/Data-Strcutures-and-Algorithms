class Solution:
    def findLHS(self, nums: List[int]) -> int:

        frequencies = {}

        for num in nums: 
            if num not in frequencies:
                frequencies[num] = 1
            else: 
                frequencies[num] += 1
        
        result = []
        for key in frequencies.keys():
            target = key - 1
            if target in frequencies:
                sum = frequencies[key] + frequencies[target]
                result.append(sum)

        return max(result) if result else 0