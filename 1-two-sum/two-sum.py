# testing
class Solution(object):
    def twoSum(self, nums, target):
        map = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in map:
                return index, map[diff]
            map[value] = index

# Time: O(n) - iterate over the array once O(n) + look up value O(n) = O(n)
# Space: O(n) - hashmap to store n elements in worst case