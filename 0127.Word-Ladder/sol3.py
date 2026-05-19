class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1

        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        word_set.discard(beginWord)

        begin_frontier = {beginWord}
        end_frontier = {endWord}
        level = 1
        word_len = len(beginWord)
        letters = "abcdefghijklmnopqrstuvwxyz"

        while begin_frontier and end_frontier:
            if len(begin_frontier) > len(end_frontier):
                begin_frontier, end_frontier = end_frontier, begin_frontier

            next_frontier = set()
            for word in begin_frontier:
                for i in range(word_len):
                    prefix = word[:i]
                    suffix = word[i + 1 :]
                    original = word[i]
                    for ch in letters:
                        if ch == original:
                            continue
                        candidate = prefix + ch + suffix
                        if candidate in end_frontier:
                            return level + 1
                        if candidate in word_set:
                            word_set.remove(candidate)
                            next_frontier.add(candidate)

            begin_frontier = next_frontier
            level += 1

        return 0
