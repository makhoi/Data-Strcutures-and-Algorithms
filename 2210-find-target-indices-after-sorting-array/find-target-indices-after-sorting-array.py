class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)

        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        if nums[left] == target:
            leftRes = left
        else:
            return []
        
        left = 0 
        right = n - 1

        while left < right:
            mid = right - (right - left) // 2

            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        
        if nums[right] == target:
            rightRes = right
        else: 
            return []

        res = []
        for index in range(leftRes, rightRes + 1):
            res.append(index)
        
        return res