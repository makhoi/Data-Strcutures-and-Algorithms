class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(h):
            l = 0
            number_frequency = {}
            count = 0

            for r in range(len(nums)):
                number_frequency[nums[r]] = number_frequency.get(nums[r], 0) + 1

                while len(number_frequency) > h:
                    number_frequency[nums[l]] -= 1
                    if number_frequency[nums[l]] == 0:
                        del number_frequency[nums[l]]
                    l += 1
                
                count += r - l + 1
            
            return count
            
        return atMost(k) - atMost(k-1)