class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        
        n = len(nums)

        average = sum/n
        
        full = []
        smallest = min(nums)
        largest = max(nums)
        for num in range(smallest, largest+2):
            full.append(num)

        result = []
        for num in full:
            if num > average and num not in nums and num > 0:
                result.append(num)
        return min(result) if result else 1