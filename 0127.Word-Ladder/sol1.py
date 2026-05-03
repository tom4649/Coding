import heapq


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def is_adjacent(w1, w2):
            if len(w1) != len(w2):
                return False
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        idx_endWord = -1
        for i, w in enumerate(wordList):
            if w == endWord:
                idx_endWord = i
                break
        if idx_endWord == -1:
            return 0

        wordList.append(beginWord)
        n = len(wordList)
        adjacent_matrix = [[] for _ in range(n)]
        for i in range(n - 1):
            wi = wordList[i]
            for j in range(i + 1, n):
                if is_adjacent(wi, wordList[j]):
                    adjacent_matrix[i].append(j)
                    adjacent_matrix[j].append(i)

        INF = float("inf")
        costs = [INF] * n
        costs[-1] = 0
        cost_heap = [(0, n - 1)]
        while cost_heap:
            c, v = heapq.heappop(cost_heap)
            if c > costs[v]:
                continue
            if v == idx_endWord:
                return c + 1
            for i in adjacent_matrix[v]:
                if c + 1 < costs[i]:
                    costs[i] = c + 1
                    heapq.heappush(cost_heap, (costs[i], i))
        return costs[idx_endWord] + 1 if costs[idx_endWord] != INF else 0
