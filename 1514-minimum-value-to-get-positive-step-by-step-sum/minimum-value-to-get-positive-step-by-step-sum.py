class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start_value = 1

        while True: 
            valid = True
            prefix_sum = start_value
            for num in nums: 
                prefix_sum += num
                if prefix_sum < 1: 
                    valid = False
                    break
            
            if valid:
                return start_value

            start_value += 1
            