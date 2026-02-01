class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)

        last_index = len(nums) - 1

        for current_index in range(len(nums)):
            step = nums[current_index]

            if step < 0: 
                # next_index = current_index - abs(step)
                # if next_index < 0: 
                #     next_index = abs(step) - current_index - 1 + last_index
                # next_value = nums[next_index]
                # result[current_index] = next_value
                result[current_index] = nums[(current_index +nums[current_index])%len(nums)]

            elif step > 0: 
                # next_index = current_index + step
                # if next_index > last_index:
                #     next_index = current_index + step - last_index - 1
                # next_value = nums[next_index]
                # result[current_index] = next_value
                result[current_index] = nums[(current_index +nums[current_index])%len(nums)]

            else: 
                next_index = current_index
                next_value = nums[next_index]
                result[current_index] = next_value

        return result