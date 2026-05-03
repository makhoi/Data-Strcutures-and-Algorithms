class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i]

        postfix = [1]*n
        postfix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i+1]*nums[i]

        res = [1]*n
        for i in range(n):
            res[i] = (prefix[i-1] if i else 1)*(postfix[i+1] if i != n - 1 else 1)
        
        return res