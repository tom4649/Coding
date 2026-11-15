import collections

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

def words_abbreviation(words: list[str]) -> list[str]:
    res = [""] * len(words)
    groups = collections.defaultdict(list)

    # 1. 初期略称でグループ化
    for i, word in enumerate(words):
        if len(word) <= 3:
            res[i] = word
        else:
            abbr = f"{word[0]}{len(word) - 2}{word[-1]}"
            groups[abbr].append((i, word))

    # 2. 衝突したグループだけTrie木で最短プレフィックスを一発特定
    for abbr, group in groups.items():
        if len(group) == 1:
            res[group[0][0]] = abbr
            continue

        root = TrieNode()
        for _, word in group:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
                curr.count += 1

        for i, word in group:
            curr = root
            prefix_len = 0
            for ch in word:
                curr = curr.children[ch]
                prefix_len += 1
                # この文字を通る単語が自分だけになったらプレフィックス確定
                if curr.count == 1:
                    break

            if len(word) - prefix_len - 1 <= 1:
                res[i] = word
            else:
                res[i] = f"{word[:prefix_len]}{len(word) - prefix_len - 1}{word[-1]}"

    return res

if __name__ == "__main__":
    words = input().split()
    res = words_abbreviation(words)
    print(" ".join(res))
