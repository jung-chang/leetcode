# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

from collections import defaultdict
from typing import List


class Solution:
    """
    You are given a list of songs where the ith song has a duration of time[i] seconds.

    Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
    """

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod_to_song = defaultdict(list)
        for song, duration in enumerate(time):
            mod_to_song[duration % 60].append(song)

        print(mod_to_song)

        pairs = set()
        for song, duration in enumerate(time):
            need = 60 - (duration % 60)
            for song_pair in mod_to_song[need]:
                pair = tuple(sorted([song, song_pair]))
                if pair not in pairs and song_pair != song:
                    pairs.add(pair)
        print(pairs)
        return len(pairs)


time = [30, 20, 150, 100, 40]
print(Solution().numPairsDivisibleBy60(time))
