from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        subword_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                subword = word[:i] + "*" + word[i + 1 :]
                subword_to_words[subword].append(word)

        frontier = {beginWord}
        seen = {beginWord}
        length = 1

        while frontier:
            next_frontier = set()
            for word in frontier:
                if word == endWord:
                    return length

                for i in range(len(word)):
                    subword = word[:i] + "*" + word[i + 1 :]
                    for neighbor in subword_to_words[subword]:
                        if neighbor not in seen:
                            next_frontier.add(neighbor)
                            seen.add(neighbor)
                    subword_to_words[subword] = []

            frontier = next_frontier
            length += 1

        return 0
