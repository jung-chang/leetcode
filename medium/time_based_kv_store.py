# https://leetcode.com/problems/time-based-key-value-store/


from collections import defaultdict


class TimeMap:
    """
    Design a time-based key-value data structure that can store multiple values for the same key at
    different time stamps and retrieve the key's value at a certain timestamp.

    Implement the TimeMap class:
        TimeMap() Initializes the object of the data structure.
        void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
        String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev.
        If there are no values, it returns "".

    """

    def __init__(self):
        self.key_to_time_map = defaultdict(lambda: {})
        self.key_to_timestamps = defaultdict(list)

    def _search_time_key(self, key: str, timestamp: int) -> int:
        timestamps = self.key_to_timestamps[key]

        # [1 2 3 4 5]
        left = 0
        right = len(timestamps)
        while left < right:
            mid = (left + right) // 2
            if timestamp > timestamps[mid]:
                left = mid + 1
            elif timestamp < timestamps[mid]:
                right = mid
        return None if right == 0 else timestamps[right - 1]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_time_map[key][timestamp] = value
        # Timestamps are always ascending
        self.key_to_timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        time_map = self.key_to_time_map[key]
        if not time_map:
            return ""
        if timestamp in time_map:
            return time_map[timestamp]
        time_key = self._search_time_key(key, timestamp)
        if time_key is None:
            return ""
        return time_map[time_key]


timemap = TimeMap()
timemap.set("love", "high", 10)
timemap.set("love", "low", 20)
print(timemap.get("love", 5))
print(timemap.get("love", 10))
print(timemap.get("love", 15))
print(timemap.get("love", 20))
print(timemap.get("love", 25))
