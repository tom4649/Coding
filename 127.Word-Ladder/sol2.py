from collections import defaultdict


class NeighborWords:
    def __init__(self):
        self.subword_to_words = defaultdict(list)

    @classmethod
    def from_words(cls, words):
        neighbor_words = NeighborWords()
        for word in words:
            neighbor_words.add(word)
        return neighbor_words

    @staticmethod
    def to_subwords(word):
        for i in range(len(word)):
            yield (word[:i], word[i + 1 :])

    def add(self, word):
        for subword in self.to_subwords(word):
            self.subword_to_words[subword].append(word)

    def iter_all(self, word):
        for subword in self.to_subwords(word):
            yield from self.subword_to_words[subword]


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbor_words = NeighborWords.from_words(wordList)
        to_visit = {beginWord}
        level = 1
        visited = set()
        while to_visit:
            next_to_visit = set()
            for word in to_visit:
                if word == endWord:
                    return level
                if word in visited:
                    continue
                for neighbor in neighbor_words.iter_all(word):
                    next_to_visit.add(neighbor)
                visited.add(word)
            to_visit = next_to_visit
            level += 1
        return 0
