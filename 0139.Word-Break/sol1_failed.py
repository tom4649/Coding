class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        stripped_sub_strs = []
        for word in wordDict:
            if s.startswith(word):
                stripped_sub_strs.append(s[len(word) :])
        return any(
            [
                self.wordBreak(stripped_sub_str, wordDict)
                for stripped_sub_str in stripped_sub_strs
            ]
        )
