from itertools import islice


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        def pair(i, j):
            return (nums1[i], nums2[j])

        def generate_line(j):
            for i in range(len(nums1)):
                yield pair(i, j)
            yield (float("inf"), float("inf"))

        def generate_range(j, j_max):
            if j >= j_max:
                yield (float("inf"), float("inf"))
            if j == j_max - 1:
                yield from generate_line(j)
            j_middle = (j + j_max) // 2
            generate_former = generate_range(j, j_middle)
            generate_latter = generate_range(j_middle, j_max)
            for _ in range(j_middle - j):
                yield next(generate_former)
            former = next(generate_former)
            latter = next(generate_latter)
            while 1:
                if sum(former) <= sum(latter):
                    yield former
                    former = next(generate_former)
                else:
                    yield latter
                    latter = next(generate_latter)

        return list(islice(generate_range(0, len(nums2)), k))
