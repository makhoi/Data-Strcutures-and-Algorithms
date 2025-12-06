class NumArray:
    def __init__(self, nums: List[int]):
        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        self.prefix_sum = prefix_sum
        
    def sumRange(self, left: int, right: int) -> int:
        ps = self.prefix_sum

        if left == 0:
            return ps[right]
        else: 
            return ps[right] - ps[left-1]
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)