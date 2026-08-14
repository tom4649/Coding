import random

class Solution:

    def __init__(self, weights: list[int]):
        n = len(weights)
        total = sum(weights)
        scaled_prob = [w * n / total for w in weights]

        self.prob = [0.0] * n
        self.alias = [0] * n
        self.n = n

        small, large = [], []
        for i, p in enumerate(scaled_prob):
            if p < 1.0:
                small.append(i)
            else:
                large.append(i)

        while small and large:
            s = small.pop()
            l = large.pop()
            self.prob[s] = scaled_prob[s]
            self.alias[s] = l
            scaled_prob[l] -= 1.0 - scaled_prob[s]
            if scaled_prob[l] < 1.0:
                small.append(l)
            else:
                large.append(l)

        while large:
            self.prob[large.pop()] = 1.0
        while small:
            self.prob[small.pop()] = 1.0

    def pickIndex(self) -> int:
        i = random.randint(0, self.n - 1)
        return i if random.random() < self.prob[i] else self.alias[i]
