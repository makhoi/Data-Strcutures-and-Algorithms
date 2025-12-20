class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for index, integer in enumerate(nums): 
            if integer in seen:
                if abs(index - seen[integer]) <= k:
                    return True
            
            seen[integer] = index

        return False
