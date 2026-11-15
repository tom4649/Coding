import collections
import re

def words_abbreviation(words: list[str]) -> list[str]:
    abbreviation_to_words = collections.defaultdict(list)
    for i, word in enumerate(words):
        if len(word) <= 3:
            abbreviation_to_words[word].append((i, word))
            continue
        abbreviation_to_words[word[0] + str(len(word) - 2) + word[-1]].append((i, word))

    def update_abbreviation(abbreviation, group):
        match = re.search(r"([A-Za-z]+)(\d+)(([A-Za-z]+))", abbreviation)
        number = int(match.group(2))
        if number == 2:
            return group

        pattern = fr"{match.group(1)}([A-Za-z]+){match.group(3)}"
        abbreviation_to_words_updated = collections.defaultdict(list)
        for i, word in group:
            match_for_word = re.search(pattern, word)
            abbreviation_updated = match.group(1) + match_for_word.group(1)[0] + str(number - 1) + match.group(3)
            abbreviation_to_words_updated[abbreviation_updated].append((i, word))

        abbreviations = []
        for updated_abbreviation, updated_group in abbreviation_to_words_updated.items():
            if len(updated_group) > 1:
                abbreviations.extend(update_abbreviation(updated_abbreviation, updated_group))
            else:
                abbreviations.append((updated_group[0][0], updated_abbreviation))

        return abbreviations

    abbreviations = []
    for abbreviation, group in abbreviation_to_words.items():
        if len(group) > 1:
            abbreviations.extend(update_abbreviation(abbreviation, group))
        else:
            abbreviations.append((group[0][0], abbreviation))
    abbreviations.sort()
    return [abbreviation[1] for abbreviation in abbreviations]

if __name__ == "__main__":
    words = input().split()
    res = words_abbreviation(words)
    print(" ".join(res))
