from collections import defaultdict

NUM_POSSIBLE_CHARS = 26
START_CHAR = "a"
ORD_START_CHAR = ord(START_CHAR)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def str_to_frequency(input_str):
            frequency = [0] * NUM_POSSIBLE_CHARS
            for input_char in input_str:
                ord_input_char_rel = ord(input_char) - ORD_START_CHAR
                if ord_input_char_rel >= NUM_POSSIBLE_CHARS:
                    raise ValueError
                frequency[ord_input_char_rel] += 1
            return tuple(frequency)

        frequency_to_strs = defaultdict(list)
        for input_str in strs:
            frequency_to_strs[str_to_frequency(input_str)].append(input_str)
        return list(frequency_to_strs.values())
