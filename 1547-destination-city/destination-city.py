class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arrivals = {}

        for cityA, cityB in paths: 
            arrivals[cityA] = cityB

        for cityB in arrivals.values(): 
            if cityB not in arrivals: 
                return cityB