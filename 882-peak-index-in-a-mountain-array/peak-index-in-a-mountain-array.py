class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        '''
        Find first appearance of element where arr[i] > arr[i+1]
        '''
        n = len(arr)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] > (arr[mid+1] if mid <= n - 1 else float('-inf')):
                right = mid
            else:
                left = mid + 1
        return left