class Solution:
    def findValidPair(self, s: str) -> str:
        nums = []
        for ch in s:
            nums.append(int(ch))

        number_frequency = {}
        for num in nums:
            number_frequency[num] = number_frequency.get(num, 0) + 1

        valid_pair = []
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1] and nums[i] == number_frequency[nums[i]] and nums[i+1] == number_frequency[nums[i+1]]:
                valid_pair.append(str(nums[i]))
                valid_pair.append(str(nums[i+1]))
                break

        return "".join(valid_pair) if valid_pair else ""