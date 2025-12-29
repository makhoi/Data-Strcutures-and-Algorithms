
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        '''
        nums[j] - nums[i] = diff
        nums[k] - nums[j] = diff

        Cô lập nums[i] và nums[j] về nums[k] và diff
        nums[j] = nums[k] - diff
        nums[i] = nums[j] - diff = nums[k] - 2*diff
        '''
        arithmetic_triplets_count = 0

        for k, x in enumerate(nums):
            left = nums[:k]
            if (x - diff) in left and (x - 2*diff) in left:
                arithmetic_triplets_count += 1

        return arithmetic_triplets_count

        