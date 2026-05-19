class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        frontier = [0]
        visited = {0}
        while frontier:
            start_position = frontier.pop()
            if start_position == len(s):
                return True
            for word in wordDict:
                new_position = start_position + len(word)
                if new_position in visited:
                    continue
                if s[start_position:new_position] != word:
                    continue
                frontier.append(new_position)
                visited.add(new_position)

        return False
