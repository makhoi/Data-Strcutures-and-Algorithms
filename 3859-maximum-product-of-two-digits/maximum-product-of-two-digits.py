class Solution:
    def maxProduct(self, n: int) -> int:
        number = str(n)
        products = []
        for i in range(len(number)):
            for j in range(i+1, len(number)):
                products.append(int(number[i]) * int(number[j]))

        return max(products)