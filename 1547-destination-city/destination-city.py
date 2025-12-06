class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        possible_routes = {}

        for cityA, cityB in paths: 
            possible_routes[cityA] = cityB

        for destination in possible_routes.values():
            if destination not in possible_routes:
                return destination