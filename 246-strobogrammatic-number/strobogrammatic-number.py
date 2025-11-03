class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatics = {
            '6':'9',
            '9':'6',
            '8':'8',
            '1':'1',
            '0':'0'
        }

        new_num = []

        for index in range(len(num)):
            if num[index] not in strobogrammatics:
                return False
            else: 
                new_num.append(strobogrammatics[num[index]])
        reversed_num = new_num[::-1]
        result = "".join(reversed_num)
        if result == num:
            return True
        return False