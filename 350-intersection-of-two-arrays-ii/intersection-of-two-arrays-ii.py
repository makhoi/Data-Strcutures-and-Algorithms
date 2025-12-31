class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:   
        nums1_occurences = {}
        for num in nums1: 
            nums1_occurences[num] = nums1_occurences.get(num, 0) + 1

        intersection = []
        for num in nums2: 
            if num in nums1_occurences and nums1_occurences[num] != 0: 
                nums1_occurences[num] -= 1
                intersection.append(num)
        
        return intersection