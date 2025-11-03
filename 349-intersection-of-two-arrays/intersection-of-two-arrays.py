class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        hashmap = {}

        for element in nums1_set: 
            if element not in hashmap: 
                hashmap[element] = None
        
        result = []

        for element in nums2_set: 
            if element in hashmap: 
                result.append(element)

        return result