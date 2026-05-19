class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        frontier = {beginWord}
        word_set.discard(beginWord)
        length = 1
        letters = "abcdefghijklmnopqrstuvwxyz"

        while frontier:
            next_frontier = set()
            for word in frontier:
                if word == endWord:
                    return length

                word_chars = list(word)
                for i in range(len(word_chars)):
                    original = word_chars[i]
                    for letter in letters:
                        if letter == original:
                            continue
                        word_chars[i] = letter
                        candidate = "".join(word_chars)
                        if candidate in word_set:
                            next_frontier.add(candidate)
                            word_set.remove(candidate)
                    word_chars[i] = original

            frontier = next_frontier
            length += 1

        return 0
