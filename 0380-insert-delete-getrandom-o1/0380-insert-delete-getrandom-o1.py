class RandomizedSet:

    def __init__(self):
        self.nums = []          # stores values
        self.pos = {}           # value -> index in nums

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False

        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        index = self.pos[val]
        last_val = self.nums[-1]

        # Put last element at removed element's place
        self.nums[index] = last_val
        self.pos[last_val] = index

        # Remove last element
        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        import random
        return random.choice(self.nums)