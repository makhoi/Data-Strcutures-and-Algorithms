class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        sum of array after removal operations = original total - x 
        find the max length of the subarray that has k = original total - x 

        ps[i] = S 
        ps[j,i] = k = original - x
        ps[j-1] = S - k

        instead of return max_length, here we returns min k 
        '''
        prefix_sum = 0
        prefix_map = {}
        total = 0
        max_length = 0
        n = len(nums)
        min_operation = 0

        for i in range(n):
            total += nums[i]

        k = total - x

        if k == 0:
            return len(nums)

        for i in range(n):
            prefix_sum += nums[i]

            if prefix_sum == k:
                max_length = max(max_length, i + 1)

            if prefix_sum - k in prefix_map:
                jM1 = prefix_map[prefix_sum-k]
                j = jM1 + 1
                l = i - j +1
                max_length = max(max_length, l)

            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

            min_operation = n - max_length

        return min_operation if max_length else -1