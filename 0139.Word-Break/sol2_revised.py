class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        stack = [0]
        visited = {0}
        while stack:
            start_position = stack.pop()
            if start_position == len(s):
                return True
            for word in wordDict:
                next_position = start_position + len(word)
                if next_position in visited:
                    continue
                if not s.startswith(word, start_position):
                    continue
                stack.append(next_position)
                visited.add(next_position)

        return False
