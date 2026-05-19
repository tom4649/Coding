class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        frontier = [0]
        visited = {0}

        while frontier:
            start = frontier.pop()
            if start == len(s):
                return True
            for word in wordDict:
                new_start = start + len(word)
                if new_start in visited:
                    continue
                if not s.startswith(word, start):
                    continue
                visited.add(new_start)
                frontier.append(new_start)

        return False
