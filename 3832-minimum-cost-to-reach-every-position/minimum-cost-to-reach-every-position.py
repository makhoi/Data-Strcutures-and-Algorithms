class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = [0]*len(cost)
        ans[0] = cost[0]
        for i in range(1, len(cost)):
            if cost[i-1] < cost[i]:
                ans[i] = cost[i-1]
                cost[i] = cost[i-1]
            else:
                ans[i] = cost[i]

        return ans