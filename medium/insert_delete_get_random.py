# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:
    """
    RandomizedSet() Initializes the RandomizedSet object.

    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.

    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.

    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called).
    Each element must have the same probability of being returned.

    """

    # def __init__(self):
    #     self.vals = set()

    # def insert(self, val: int) -> bool:
    #     if val in self.vals:
    #         return False
    #     self.vals.add(val)
    #     return True

    # def remove(self, val: int) -> bool:
    #     if val not in self.vals:
    #         return False
    #     self.vals.remove(val)
    #     return True

    # def getRandom(self) -> int:
    #     return random.choice(list(self.vals))

    def __init__(self):
        self.vals_to_i = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.vals_to_i:
            return False
        self.vals_to_i[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.vals_to_i:
            return False

        # Swap with last and pop
        i = self.vals_to_i[val]
        last = self.vals[-1]
        self.vals[i] = last
        self.vals_to_i[last] = i
        self.vals.pop()
        self.vals_to_i.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
