class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(h):
            res = 0
            odd_count = 0
            left = 0

            for right in range(len(nums)):
                odd_count += 1 if nums[right] % 2 == 1 else 0

                while odd_count > h:
                    odd_count -= 1 if nums[left] % 2 == 1 else 0
                    left += 1
                
                res += right - left + 1
            
            return res
            
        return atMost(k) - atMost(k-1)