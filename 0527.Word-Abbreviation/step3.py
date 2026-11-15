import collections

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def words_abbreviation(words: list[str]) -> list[str]:
    abbreviations = [""] * len(words)
    abbreviation_to_words = collections.defaultdict(list)

    for i, word in enumerate(words):
        if len(word) <= 3:
            abbreviations[i] = word
            continue
        abbreviation = word[0] + str(len(word) - 2) + word[-1]
        abbreviation_to_words[abbreviation].append((i, word))

    for abbreviation, group in abbreviation_to_words.items():
        if len(group) == 1:
            abbreviations[group[0][0]] = abbreviation
            continue

        root = TrieNode()
        for _, word in group:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.count += 1

        for i, word in group:
            node = root
            len_prefix = 1
            for ch in word:
                node = node.children[ch]
                if node.count == 1:
                    break
                len_prefix += 1

            if len(word) - len_prefix - 1 <= 1:
                abbreviations[i] = word
            else:
                abbreviations[i] = word[:len_prefix]+ str(len(word) - len_prefix - 1) + word[-1]

    return abbreviations








if __name__ == "__main__":
    words = input().split()
    res = words_abbreviation(words)
    print(" ".join(res))
