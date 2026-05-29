class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        result = []
        broken_words = []

        def traverse(start):
            if start == len(s):
                result.append(" ".join(broken_words))
                return
            for word in wordDict:
                if s.startswith(word, start):
                    broken_words.append(word)
                    traverse(start + len(word))
                    broken_words.pop()

        traverse(0)
        return result
