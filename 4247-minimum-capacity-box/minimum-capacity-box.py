class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        capacity_index = defaultdict(list)
        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                capacity_index[capacity[i]].append(i)

        if capacity_index != {}:
            min_capacity = min(capacity_index.keys())
            return capacity_index[min_capacity][0]
        return -1