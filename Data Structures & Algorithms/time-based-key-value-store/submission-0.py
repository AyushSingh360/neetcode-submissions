from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        # key -> list of (timestamp, value)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamps for a key are non-decreasing, so append keeps list sorted
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]  # list of (t, v)
        # We want the index of the largest t <= timestamp.
        # We'll binary search on the timestamps only.
        i = bisect.bisect_right(arr, (timestamp, chr(127)))  # sentinel to go to the rightmost

        if i == 0:
            return ""
        return arr[i - 1][1]