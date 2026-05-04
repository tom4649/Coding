import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def next_permutation(sequence):
            n = len(sequence)
            pivot = -1

            for i in range(n - 1, 0, -1):
                if sequence[i] > sequence[i - 1]:
                    pivot = i - 1
                    break

            if pivot == -1:
                return False

            for j in range(n - 1, pivot, -1):
                if sequence[j] > sequence[pivot]:
                    sequence[pivot], sequence[j] = sequence[j], sequence[pivot]
                    sequence[pivot + 1 :] = reversed(sequence[pivot + 1 :])
                    return True

        nums_sorted = sorted(nums)
        permutations = [nums_sorted.copy()]
        while next_permutation(nums_sorted):
            permutations.append(nums_sorted.copy())

        return permutations
