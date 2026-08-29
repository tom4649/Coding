import random

class Solution:

    def __init__(self, weights: list[int]):
        self.n = len(weights)
        total = sum(weights)
        scaled_weights = [w / total * self.n for w in weights]

        self.prob = [0.0] * self.n
        self.alias = [0] * self.n

        small = []
        large = []
        for i, p in enumerate(scaled_weights):
            if p < 1.0:
                small.append(i)
            else:
                large.append(i)

        while small and large:
            i_small = small.pop()
            i_large =large.pop()
            self.alias[i_small] = i_large
            self.prob[i_small] =  scaled_weights[i_small]
            scaled_weights[i_large] -= 1.0 - scaled_weights[i_small]
            if scaled_weights[i_large] < 1.0:
                small.append(i_large)
            else:
                large.append(i_large)

        while large:
            i = large.pop()
            self.prob[i] = 1.0
        while small:
            i = small.pop()
            self.prob[i] = 1.0


    def pickIndex(self) -> int:
        i = random.randint(0, self.n - 1)
        return i if random.random() < self.prob[i] else self.alias[i]
