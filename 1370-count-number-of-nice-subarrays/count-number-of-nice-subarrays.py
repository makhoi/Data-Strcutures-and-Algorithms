class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(h):
            count = 0
            odd_count = 0
            left = 0

            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    odd_count += 1

                while odd_count > h:
                    if nums[left] % 2 != 0:
                        odd_count -= 1
                    left += 1 
                
                count += right - left + 1
            
            return count

        return atMost(k) - atMost(k-1)