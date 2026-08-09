import random


def sort_colors(nums: list[int], k: int) -> None:
    starts = [0] * k

    for i, val in enumerate(nums):
        index_to_move = i
        for color in range(k - 1, val - 1, -1):
            nums[starts[color]], nums[index_to_move] = (
                nums[index_to_move],
                nums[starts[color]],
            )
            index_to_move = starts[color]
            starts[color] += 1


k = 20

test_cases = [[random.randint(0, k - 1) for _ in range(20)] for _ in range(20)]

for test_case in test_cases:
    colors = test_case.copy()
    sort_colors(colors, k)
    assert colors == sorted(test_case)
