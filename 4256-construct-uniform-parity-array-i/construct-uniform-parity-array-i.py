class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        '''
        
        case 1: nums1 contains all even number
        -> at every i, do nums2[i] = nums1[i] -> all nums2 contains even number -> True
        or
        -> at every i, do nums2[i] = nums1[i] - nums[j] = even - even = even -> all nums2 contains even numbers -> True
        
        case 3: num1 contains all odd numbers
        -> at every i, do nums2[i] = nums1[i] -> nums2 contains all odd number -> True
        or
        -> at evedy i, do nums2[i] = nums1[i] - nums1[j] = odd - odd = odd -> nums2 contains all odd number -> True
        
        case 2: even and odd
        a) even count > odd count: 
        -> at i, if nums1[i] is even, let nums2[i] = nums1[i] - nums1[j] where nums1[j] is an odd number, if nums1[i] is odd -> do nums2[i] = nums1[i] -> nums2 contains all odd number -> True
        b) even count < odd count
        -> at i, if nums1[i] is even, let nums2[i] = nums1[i] - nums1[j] where nums1[j] is an odd number, if nums1[i] is odd -> do nums2[i] = nums1[i] -> nums2 contains all odd number -> True
        or
        -> at i, if nums1[i] is even, let nums2[i] = nums1[i], if nums1[i] is odd -> do nums2[i] = nums1[i] - nums1[j] where nums1[j] is an odd value = odd - odd = even -> nums2 contains all even number -> True
        Hence, every cases are possible -> return True
        '''
        return True