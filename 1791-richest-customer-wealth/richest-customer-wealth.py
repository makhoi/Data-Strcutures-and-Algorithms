class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        left, right = 0, len(accounts[0]) - 1
        top, bottom = 0, len(accounts) - 1

        total = 0
        customers_wealth = []
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                total += accounts[r][c]
            customers_wealth.append(total)
            total = 0

        return max(customers_wealth)