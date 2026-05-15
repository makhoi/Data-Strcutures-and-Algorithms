class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []

        for i in range(len(mountain)):
            if mountain[i] > (mountain[i-1] if i > 0 else float('-inf')) and mountain[i] > (mountain[i+1] if i < len(mountain) - 1 else float('-inf')):
                if i != 0 and i != len(mountain) - 1:
                    peaks.append(i)
        return peaks