class Solution:
    def minimumFlips(self, n: int) -> int:
        '''
        Convert number to binary number
        Determine its reverse version
        Convert that reverse version in binary number to integer number
        Compare between original binary num and reversed binary num, one by one element -> if different add 1 to count
        '''
        binary_num = f"{n:b}"

        reverse_binary_array = []
        for i in range(len(binary_num)-1, -1, -1):
            reverse_binary_array.append(binary_num[i])
        reversed_binary_num = "".join(reverse_binary_array)
        
        flip_count = 0
        for i in range(len(binary_num)):
            if binary_num[i] != reverse_binary_array[i]:
                flip_count += 1
        return flip_count


