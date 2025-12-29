class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        arrivals = {}
        for cityA, cityB in paths: 
            arrivals[cityA] = cityB

        for arrival in arrivals.values():
            if arrival not in arrivals:
                return arrival