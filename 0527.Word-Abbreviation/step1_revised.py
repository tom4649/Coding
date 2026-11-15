import collections

def words_abbreviation(words: list[str]) -> list[str]:
    abbreviations = [""] * len(words)

    def update_abbreviation(items, len_prefix):
        groups = collections.defaultdict(list)
        for i, word in items:
            if len(word) - len_prefix <= 2:
                abbreviation = word
            else:
                abbreviation = f"{word[:len_prefix]}{len(word) - len_prefix - 1}{word[-1]}"
            groups[abbreviation].append((i, word))

        for abbreviation, group in groups.items():
            if len(group) == 1 or abbreviation == group[0][1]:
                for i, _ in group:
                    abbreviations[i] = abbreviation
            else:
                update_abbreviation(group, len_prefix + 1)

    update_abbreviation(list(enumerate(words)), 1)
    return abbreviations

if __name__ == "__main__":
    words = input().split()
    res = words_abbreviation(words)
    print(" ".join(res))
