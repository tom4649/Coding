import collections


class TimeMap:
    def __init__(self):
        self.key_to_value_and_timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_value_and_timestamps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.key_to_value_and_timestamps[key])

        while left < right:
            mid = left + (right - left) // 2
            # timestamps[left - 1] <= timestamp
            # timestamps[right] > timestamp
            if self.key_to_value_and_timestamps[key][mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid

        return "" if left == 0 else self.key_to_value_and_timestamps[key][left - 1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
