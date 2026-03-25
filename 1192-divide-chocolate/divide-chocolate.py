'''
1. lowerbound vs upperbound: find possible maximum of minimun level of sweetness -> find last T -> find last appearance of target -> upperbound
2. search space: 
- lowerbound: min(sweetness)
- upperbound: sum(sweetness) // (k+1)
why? 
let S be sum(sweetness)
    we split into k+1 pieces
If the minimum piece sweetness is x, then every piece must be >= x.
    <=> S >= x(k+1)
    <=> x <= S/(k+1)
    hence search space is [min(sweetness),sum(sweetness)//(k+1)]
if you push it above average, total sum is insufficient to support all k+1 pieces.
3. condition to move left: if canSplit(mid) == True
4. meaning of right: min right satisfies the condition
5. result: return right
'''
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def canSplit(minSweetness):
            current_sweet = 0
            split_count = 0
            for s in sweetness:
                current_sweet += s
                if current_sweet >= minSweetness:
                    split_count += 1
                    current_sweet = 0
            return split_count >= k + 1 
        
        left = min(sweetness)
        right = sum(sweetness)//(k+1)

        while left < right: 
            mid = right - (right-left)//2
            '''
            l     m    r
            TTTTTFFFFFFF
            '''
            if canSplit(mid):
                left = mid
            else:
                right = mid - 1
        return right
