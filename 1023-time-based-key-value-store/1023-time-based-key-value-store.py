class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        data = self.store[key]
        low , high = 0 , len(data) - 1

        result_value = ""

        while low <= high:
            mid = (low+high) // 2
            mid_time = data[mid][0]

            if mid_time == timestamp:
                return data[mid][1]

            elif mid_time < timestamp: 
                result_value = data[mid][1]

                low = mid+1
            else:
                high = mid - 1
        return result_value
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)