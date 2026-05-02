class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(h):
            count = 0
            number_frequency = {}
            left = 0

            for right in range(len(nums)):
                number_frequency[nums[right]] = number_frequency.get(nums[right], 0) + 1
                num_count = len(number_frequency)

                while len(number_frequency) > h:
                    number_frequency[nums[left]] -= 1
                    if number_frequency[nums[left]] == 0:
                        del number_frequency[nums[left]]
                        num_count -= 1
                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k-1)