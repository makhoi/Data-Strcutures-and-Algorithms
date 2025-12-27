class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total = 0
        customers_wealth = []

        for account in accounts:
            for amount in account:
                total += amount
            customers_wealth.append(total)
            total = 0
        
        return max(customers_wealth)