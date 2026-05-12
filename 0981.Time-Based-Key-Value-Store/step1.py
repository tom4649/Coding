import bisect


class TimeMap:
    def __init__(self):
        self.key_to_values = {}
        self.key_to_timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_values.setdefault(key, []).append(value)
        self.key_to_timestamps.setdefault(key, []).append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not self.key_to_timestamps.get(key, []):
            return ""
        if timestamp < self.key_to_timestamps[key][0]:
            return ""

        index = bisect.bisect_right(self.key_to_timestamps[key], timestamp) - 1
        return self.key_to_values[key][index]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
