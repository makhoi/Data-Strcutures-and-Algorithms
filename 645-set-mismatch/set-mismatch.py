class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)

        frequency = {}
        for num in nums: 
            if num not in frequency: 
                frequency[num] = 1 
            else: 
                frequency[num] += 1

        # Get duplicated number
        duplicated_number = 0
        for key, value in frequency.items():
            if value != 1:
                duplicated_number = key
        
        # Calculate expected sum
        n = len(nums)
        expected_sum = (n*(n+1))//2

        # Calculate actual sum
        actual_sum = sum(nums)

        # Missing number
        missing_number = expected_sum - (actual_sum - duplicated_number)
        # if missing_number == 0:
        #     missing_number = 2
            
        result = []
        result.append(duplicated_number)
        result.append(missing_number)

        return result