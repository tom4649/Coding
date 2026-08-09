class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length_of_longest = 0

        def update_longest(target_alphabet):
            nonlocal length_of_longest
            left = 0
            num_other_than_target = 0
            for right in range(len(s)):
                if s[right] != target_alphabet:
                    num_other_than_target += 1
                while num_other_than_target > k:
                    if s[left] != target_alphabet:
                        num_other_than_target -= 1
                    left += 1
                length_of_longest = max(length_of_longest, right - left + 1)

        for target_alphabet in set(s):
            update_longest(target_alphabet)

        return length_of_longest
