class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        odd_count = 0
        even_count = 0

        for num in nums:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return [0]*even_count + [1]*odd_count