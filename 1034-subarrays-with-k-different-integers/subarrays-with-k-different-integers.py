# Sliding Window Type 3
# TIme: O(n)
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(h):
            l = 0
            count = 0
            frequency = {}

            for r in range(len(nums)):
                frequency[nums[r]] = frequency.get(nums[r], 0) + 1

                while len(frequency) > h:
                    frequency[nums[l]] -= 1
                    if frequency[nums[l]] == 0:
                        del frequency[nums[l]]
                    l += 1

                count += r - l + 1

            return count

        return atMost(k) - atMost(k-1)