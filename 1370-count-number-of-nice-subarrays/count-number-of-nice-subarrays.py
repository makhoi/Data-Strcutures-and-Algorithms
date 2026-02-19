class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # convert odd -> 1 and even -> 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = 1
            else:
                nums[i] = 0
        
        '''
        ps[j,i] = k
        ps[i] = S
        ps[j-1] = S - k
        '''

        s = 0
        prefixMap = {}
        count = 0
        n = len(nums)

        for i in range(n):
            s += nums[i]

            if s == k:
                count += 1

            if s - k in prefixMap:
                count += prefixMap[s - k]

            prefixMap[s] = prefixMap.get(s, 0) + 1

        return count