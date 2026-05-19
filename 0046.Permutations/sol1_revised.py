import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def next_permutation(sequence):
            for i in range(len(sequence) - 1, 0, -1):
                if sequence[i] <= sequence[i - 1]:
                    continue
                for j in range(len(sequence) - 1, i - 1, -1):
                    if sequence[j] >= sequence[i - 1]:
                        sequence[i - 1], sequence[j] = sequence[j], sequence[i - 1]
                        sequence[i:] = reversed(sequence[i:])
                        return True

            return False

        nums_sorted = sorted(nums)
        permutations = [nums_sorted.copy()]
        while next_permutation(nums_sorted):
            permutations.append(nums_sorted.copy())

        return permutations
