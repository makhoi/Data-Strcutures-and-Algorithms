class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        '''
        smallest = k
        largest = largest multple of k in nums + k
        array_of_multiple_of_k = [smallest, largest + k]
        compare array_of_multiple_of_k with nums, add it to the missing array
        return the smallest number
        '''

        # find the largest multiple of k in nums 
        current_multiple = []
        for num in nums:
            if num % k == 0: 
                current_multiple.append(num)
        smallest = k
        largest = (max(current_multiple) if current_multiple else 0) + k

        full_multiple = []
        for num in range(smallest, largest + 1):
            if num % k == 0: 
                full_multiple.append(num)
        
        current_multiples = set(current_multiple)

        res = []
        for num in full_multiple: 
            if num not in current_multiples:
                res.append(num)

        return min(res)