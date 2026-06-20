class Solution:
    def constructTransformedArray(self, nums):
        '''
        The basic idea for the given formula is as follows:
        We need to start at i and move nums[i] right or left and this is denoted in the sign of i + nums[i]. We modulo it by the length len to make sure it stays within the size of the given vector, but if nums[i] is a negative number, it's possible that the result is negative. Therefore, we can add len to our result and then modulo len again, effectively doing the same modulo operation that we just did. Adding len will ensure that our result is positive, and it's mathematically valid because adding by the length of the vector puts us in the same spot (it's like walking around whole array back to where we are). Thus, we can just modulo that and get to where we need to be. Hence, ((i + nums[i]) % len + len) % len
        '''
        n = len(nums)
        return [nums[((i + nums[i]) % n + n) % n] for i in range(n)]