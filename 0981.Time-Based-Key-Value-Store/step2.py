import collections
import bisect


class TimeMap:
    def __init__(self):
        self.key_to_value_and_timestamps = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_value_and_timestamps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        index = (
            bisect.bisect_right(
                self.key_to_value_and_timestamps[key], timestamp, key=lambda x: x[1]
            )
            - 1
        )
        return "" if index == -1 else self.key_to_value_and_timestamps[key][index][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
