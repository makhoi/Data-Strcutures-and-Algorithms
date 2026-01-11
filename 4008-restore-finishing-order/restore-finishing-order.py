class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        missing = []
        for n in order: 
            if n not in friends_set:
                missing.append(n)
        
        for n in missing:
            order.remove(n)
        
        return order