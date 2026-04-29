class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        cummulative_product[i] = product[len(nums)]/cummulative_product[i-1]
        if frequency of 0 = 1: every product s 0 except at index of value 0
        if frequency of 0 > 1: every thing is 0
        '''
        number_frequency = {}
        for num in nums:
            number_frequency[num] = number_frequency.get(num, 0) + 1
        
        n = len(nums)
        cummulative_product = [0]*n
        cummulative_product[0] = nums[0]
        for i in range(1, n):
            cummulative_product[i] = cummulative_product[i-1]*nums[i]
        product = cummulative_product[n-1]

        def rightProduct(index):
            return product // cummulative_product[index]

        def leftProduct(index):
            return cummulative_product[index-1] if index != 0 else 1


        res = []
        if number_frequency.get(0,0) == 0:
            for i in range(n):
                res.append(rightProduct(i)*leftProduct(i))
        
        if number_frequency.get(0,0) == 1:
            non_zero_product = 1
            for num in nums:
                if num != 0:
                    non_zero_product *= num

            for i in range(n):
                if nums[i] == 0:
                    res.append(non_zero_product)
                else:
                    res.append(0)

        if number_frequency.get(0,0) > 1:
            res = [0]*n
        
        return res