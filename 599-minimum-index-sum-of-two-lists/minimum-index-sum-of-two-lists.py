class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        dict1 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i

        dict2 = {}
        for i in range(len(list2)):
            dict2[list2[i]] = i

        dict3 = {}
        if len(list1) >= len(list2):
            for key in dict1.keys():
                if key in dict2:
                    dict3[key] = dict1[key] + dict2[key]
        else: 
            for key in dict2.keys():
                if key in dict1:
                    dict3[key] = dict1[key] + dict2[key]

        # Given a dictionary, return the key with minimum value
        # min(d, key=d.get)  
        # 1. Find the minimum value in a dictionary:
        min_value = min(dict3.values())

        # 2. Collect all keys with that minimum value
        min_keys = [key for key, value in dict3.items() if value == min_value]
        
        return min_keys