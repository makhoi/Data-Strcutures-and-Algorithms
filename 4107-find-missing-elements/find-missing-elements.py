class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        '''
        1. Determine the range of the desired list = [smalles, largest] = [min(nums), max(nums)]
        2. set(nums) = existing
        3. for num range of the desired list:
        - num not in existing -> missing.append(num)
        return missing
        '''
        smallest = min(nums)
        largest = max(nums)

        existing = set(nums)

        missing = []
        for num in range(smallest, largest+1):
            if num not in existing:
                missing.append(num)

        return missing