class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        1. Find all subarray with length k -> n
        2. Among n, find one with average >= threshold

        or

        1. Find all subarray with length k -> n
        2. Among n, find one with average < threshold -> m
        3. return n - m 

        r starts at index k - 1

        '''
        l = 0
        count = 0
        average = 0
        sum = 0

        if len(arr) < k:
            return 0

        for r in range(len(arr)):
            sum += arr[r]

            while (r-l+1) > k:
                sum -= arr[l]
                l += 1

            average = sum/k
            
            if (r-l+1) == k and average >= threshold:
                count += 1

        return count