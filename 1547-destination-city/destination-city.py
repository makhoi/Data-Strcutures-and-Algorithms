class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        routes = {}

        for cityA, cityB in paths:
            routes[cityA] = cityB

        for arrival in routes.values():
            if arrival not in routes:
                return arrival
        