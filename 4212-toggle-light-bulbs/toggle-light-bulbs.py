class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        bulb_frequency = {}
        for bulb in bulbs:
            bulb_frequency[bulb] = bulb_frequency.get(bulb, 0) + 1

        res = []
        for bulb, frequency in bulb_frequency.items():
            if frequency % 2 == 1:
                res.append(bulb)
        
        return sorted(res)