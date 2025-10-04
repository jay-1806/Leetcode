class TimeMap:
    def __init__(self):
        # We store the data more optimally for bisect:
        # key -> [ [timestamps], [values] ]
        # This keeps the two lists parallel and avoids list-of-list lookups
        self.store = collections.defaultdict(lambda: [[], []])

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append to the parallel lists. O(1)
        self.store[key][0].append(timestamp)
        self.store[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        timestamps, values = self.store[key]
        
        # O(log L) operation using the optimized C implementation
        # 'i' is the index *after* the largest timestamp <= the target
        i = bisect.bisect_right(timestamps, timestamp)

        # Case 1: i == 0 means all timestamps are > target_timestamp (i.e., too early)
        if i == 0:
            return ""
        
        # Case 2: The largest valid timestamp is at index i - 1
        return values[i - 1]