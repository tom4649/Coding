class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        sub_strings = []
        for word in wordDict:
            if s.startswith(word):
                sub_strings.append(s[len(word) :])
        return any(
            [
                self.wordBreak(stripped_sub_str, wordDict)
                for stripped_sub_str in sub_strings
            ]
        )
