# sliding window dạng 3
# Time: O(n)
# Space: O(k)
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(h):
            l = 0 
            res = 0
            count = defaultdict(int)

            for r in range(len(nums)):
                count[nums[r]] += 1

                while len(count) > h:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                res += r - l + 1
            
            return res
        
        return atMost(k) - atMost(k-1)