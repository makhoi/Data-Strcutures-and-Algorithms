class NumArray:
    def __init__(self, nums: List[int]):
        # self.prefix_sum = [0]*len(nums)
        # self.prefix_sum[0] = nums[0]
        # for i in range(1, len(nums)): 
        #     self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i]
        # self means store this on the object so it survives after the __init__ finishes
        # anything without self. is local var and it disappears when function ends

        prefix_sum = [0]*len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)): 
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        self.prefix_sum = prefix_sum
        
    def sumRange(self, left: int, right: int) -> int:
        # if left == 0:
        #     return self.prefix_sum[right]

        # else: 
        #     return self.prefix_sum[right] - self.prefix_sum[left - 1]
    # must call self.prefix_sum because prefix_sum lives on the object (I stored it to the object on above step)
    # prefix_sum is not defined by function 
        ps = self.prefix_sum
        if left == 0:
            return ps[right]
        else: 
            return ps[right] - ps[left-1]
            
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)