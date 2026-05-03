import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_adjacent(s1, s2):
            num_different_char = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    if num_different_char > 0:
                        return False
                    num_different_char += 1
            return True

        idx_end_word = None
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                idx_end_word = i
                break
        if idx_end_word is None:
            return 0

        word_list_with_begin_word = wordList + [beginWord]
        adjacent_list = [[] for _ in range(len(wordList) + 1)]

        for i in range(len(word_list_with_begin_word)):
            for j in range(i + 1, len(word_list_with_begin_word)):
                if is_adjacent(
                    word_list_with_begin_word[i], word_list_with_begin_word[j]
                ):
                    adjacent_list[i].append(j)
                    adjacent_list[j].append(i)

        frontier = {len(word_list_with_begin_word) - 1}
        seen = {len(word_list_with_begin_word) - 1}
        length = 1

        while frontier:
            next_frontier = []
            for idx_word in list(frontier):
                if idx_word == idx_end_word:
                    return length
                for idx_adjacent in adjacent_list[idx_word]:
                    if idx_adjacent not in seen:
                        next_frontier.append(idx_adjacent)
                        seen.add(idx_adjacent)
            frontier = next_frontier
            length += 1
        return 0
