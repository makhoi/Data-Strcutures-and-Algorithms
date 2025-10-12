class NumArray:

    def __init__(self, nums: List[int]):
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        self.prefix_sum = prefix_sum
        
    def sumRange(self, left: int, right: int) -> int:
        ps = self.prefix_sum
        res = ps[right] - (ps[left-1] if left else 0)
        return res
        
