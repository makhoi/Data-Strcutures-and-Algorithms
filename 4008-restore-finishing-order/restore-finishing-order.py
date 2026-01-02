class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        '''
        Determine missing values from friend array to order 
        Remove that missing values from order array -> we got the result
        '''
        missing = []
        for o in order:
            if o not in friends: 
                missing.append(o)

        for m in missing:
            order.remove(m)
            
        return order