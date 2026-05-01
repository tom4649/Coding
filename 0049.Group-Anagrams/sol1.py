from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_sets = defaultdict(list)
        for orig_str in strs:
            sorted_str = sorted(orig_str)
            anagram_sets["".join(sorted_str)].append(orig_str)
        return list(anagram_sets.values())
