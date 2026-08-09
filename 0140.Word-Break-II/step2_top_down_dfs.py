import functools


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)

        @functools.cache
        def traverse(start):
            if start == len(s):
                return [""]

            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    sub_sentences = traverse(end)
                    for sub in sub_sentences:
                        if sub == "":
                            result.append(word)
                        else:
                            result.append(word + " " + sub)
            return result

        return traverse(0)
